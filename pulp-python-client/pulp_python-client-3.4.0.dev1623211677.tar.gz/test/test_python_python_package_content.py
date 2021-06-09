# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.python_python_package_content import PythonPythonPackageContent  # noqa: E501
from pulpcore.client.pulp_python.rest import ApiException

class TestPythonPythonPackageContent(unittest.TestCase):
    """PythonPythonPackageContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PythonPythonPackageContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_python.models.python_python_package_content.PythonPythonPackageContent()  # noqa: E501
        if include_optional :
            return PythonPythonPackageContent(
                artifact = '0', 
                relative_path = '0', 
                file = bytes(b'blah'), 
                repository = '0', 
                summary = '0', 
                description = '0', 
                description_content_type = '0', 
                keywords = '0', 
                home_page = '0', 
                download_url = '0', 
                author = '0', 
                author_email = '0', 
                maintainer = '0', 
                maintainer_email = '0', 
                license = '0', 
                requires_python = '0', 
                project_url = '0', 
                project_urls = None, 
                platform = '0', 
                supported_platform = '0', 
                requires_dist = None, 
                provides_dist = None, 
                obsoletes_dist = None, 
                requires_external = None, 
                classifiers = None
            )
        else :
            return PythonPythonPackageContent(
                relative_path = '0',
        )

    def testPythonPythonPackageContent(self):
        """Test PythonPythonPackageContent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
