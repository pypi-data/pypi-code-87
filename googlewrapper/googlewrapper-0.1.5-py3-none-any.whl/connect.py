import argparse

from oauth2client import client, tools, file
import httplib2

from pathlib import Path

from googleapiclient.discovery import build
from google.oauth2 import service_account

import pygsheets


class Connection:
    """
    Establishes authentication for google API products

    Needs the client_secret.json from the Google Developer Console
    
    Class will create a folder in the CWD (if it doesn't exist)
    Authenticate via oAuth2.0
    Return a resource object to be used in the other wrapper classes

    Current methods for authenication
    .gsc()
    .ga()
    .cal()
    .sheets()
    .gbq() * requires a separate service account authentication file * 
    .gmail()
    """
    def __init__(self, file_path="client_secret.json"):
        self.file_path = file_path
        self.dir_check()

    def dir_check(self):
        # if there isn't a crednetials folder, create one
        if not Path("./credentials/").is_dir():
            Path("./credentials/").mkdir()

    def authenticate(self, scope, token_name,http_return=True):
        """
        Authenticates Google Product using oauth2
        Saves the credentials in the ./credentials folder
        Returns the authroized resource object

        Params:
        scope: list of strings (urls from google)
            to find list of all scopes
                https://developers.google.com/identity/protocols/oauth2/scopes

        token_name: string: what we will name our crednetials.dat file

        Method is based on Google Analytics Authentication found here:
        https://developers.google.com/analytics/devguides/
            reporting/core/v4/quickstart/installed-py#3_setup_the_sample
        """
        # Parse command-line arguments.
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[tools.argparser],
        )
        flags = parser.parse_args([])

        # Set up a Flow object to be used if we need to authenticate.
        flow = client.flow_from_clientsecrets(
            self.file_path,
            scope=scope,
            message=tools.message_if_missing(self.file_path),
        )

        # Prepare credentials, and authorize HTTP object with them.
        # If the credentials don't exist or are invalid
        # run through the native client flow.
        # The Storage object will ensure that if successful the good
        # credentials will get written back to a file.
        storage = file.Storage(f"./credentials/{token_name}.dat")
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage, flags)
        
        if http_return:
            return credentials.authorize(http=httplib2.Http())

        return credentials

    def gsc(self):
        scope_list = ["https://www.googleapis.com/auth/webmasters.readonly"]
        return build(
            "webmasters", "v3", http=self.authenticate(scope_list, "search_console")
        )

    def ga(self):
        scope_list = ["https://www.googleapis.com/auth/analytics.readonly"]
        return build(
            "analyticsreporting", "v4", http=self.authenticate(scope_list, "analytics")
        )

    def cal(self):
        scope_list = ["https://www.googleapis.com/auth/calendar"]
        return build("calendar", "v3", http=self.authenticate(scope_list, "calendar"))

    def pygsheets(self):
        return pygsheets.authorize(local=True,credentials_directory='./credentials/')

    def sheets(self):
        scope_list = [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets",
        ]
        return build("sheets", "v4", http=self.authenticate(scope_list, "sheets"))

    def gbq(self, sa_file_path="gbq-sa.json"):
        return service_account.Credentials.from_service_account_file(sa_file_path)

    def gmail(self):
        scope_list = ["https://mail.google.com/"]
        return build("gmail", "v1", http=self.authenticate(scope_list, "gmail"))
