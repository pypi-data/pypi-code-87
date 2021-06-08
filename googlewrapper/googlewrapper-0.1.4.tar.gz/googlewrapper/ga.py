"""
GA CONNECTION
https://developers.google.com/analytics/
devguides/reporting/core/v4/rest/v4/reports/batchGet
"""
import pandas as pd
from googlewrapper.connect import Connection

class GoogleAnalytics:
    def __init__(self, view, auth = Connection().ga(), default_view="df"):
        """
        view: Google Analytics view ID
          type: string
        auth: Google Analytics authentication object
          type: googleapiclient.discovery.Resource object
        """
        self.auth = auth
        self.set_view(view)
        self.make_df = True if default_view == "df" else False

        # initialize filters to not be applied
        # we can add them in using the appropriate methods
        self._dim_filter = None
        self._metric_filter = None

    def set_view(self, view):

        self.viewId = view

    def set_metrics(self, m):
        """
        Parameters

        m: which ga metrics we want to use, ensure they are named correct
          type: list of strings

        for naming help:
          https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/?
        """
        self._metrics = m

    def set_dimensions(self, d):
        """
        Parameters

        d: which ga dimensions we want to use,
            ensure they are named correct
          type: list of strings

        if you would like to pull multiple days worth of data,
        and would like to maintain the time aggregation,
        remember to include one of the following:
            year, month, week, day, yearMonth, date
        or whatever breakdown you would like

        for naming help:
            https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/?
        """
        self._dims = d

    def set_dimension_filters(self, f):
        """
        Parameters
        f: all the dimension filters
          type: list of tupes
        tuple structure = (dimension name, operator,expression)

        dimensionName: dimension to be filtered
          type: str
        not:
          type: bool
          default: False
        operator: how to match
          possible values: ["REGEXP","BEGINS_WITH","ENDS_WITH",
                              "PARTIAL","EXACT","NUMERIC_EQUAL",
                              "NUMERIC_GREATER_THAN",
                              "NUMBER_LESS_THAN","IN_LIST"]
          type: str
          default: REGEXP
        expression: only first considered, unless operator is "IN_LIST"
          type: list of strings
        caseSensitive: does case matter?
          type: bool
          default False

        for more details:
          https://developers.google.com/analytics/devguides/
          reporting/core/v4/rest/v4/reports/batchGet#DimensionFilterClause
        """
        self._dim_filter = f

    def set_metric_filters(self, m):
        """
        Parameters
        m: all the metric filters
          type: list of tuples
        tuple structure = (metric name, not, operator, comparisonValue)

        metricName: name of metric to filter
          type: str
        not: True = Values Excluded, False = Values Included
          type: bool
          default: False
        operator: how you want to compare
          possible values: ["EQUAL", "LESS_THAN",
                        "GREATER_THAN","IS_MISSION"]
          type: string

        for more details:
          https://developers.google.com/analytics/devguides/
          reporting/core/v4/rest/v4/reports/batchGet#operator_1
        """
        self._metric_filter = m

    def set_start_date(self, d):
        """
        Parameters

        d: will assign s_date variable
          type: datetime
        """
        self._s_date = d

    def set_end_date(self, d):
        """
        Parameters

        d: will assign e_date variable
          type: datetime
        """
        self._e_date = d

    def build_request(self, size=100000, page_token=None, hide_totals=True, pull=True):
        """
        Parameters:

        Previously have assigned the following
         variables using their respective modules
        self._s_date: start date:
          type: datetime.date
        self._e_date: ending date:
          type: datetime.date
        self._metrics: ga metrics:
          type: list
        self._dims: ga dimensions:
          type: list

        optional (still previously assgined):
        self._dims_filter: ga filter:
          type: list of tuple

        Passed in Parameters:
        size: max number of rows to return
          type: int
          default: 100,000 (max allowed by GA)
        page_token: if you reached your max, pass this in
                     to use this as starting row
          type: str
          default: None (start at 0)
        hide_totals: if you want to see totals in the response json
          type: bool
          default: False
        pull: if after building the request json you want to call the API
          type: bool
          default: True (will request data from the GA API)

        """
        req_obj = {
            "reportRequests": [
                {
                    "viewId": str(self.viewId),
                    "dateRanges": [
                        {
                            "startDate": self._s_date.strftime("%Y-%m-%d"),
                            "endDate": self._e_date.strftime("%Y-%m-%d"),
                        }
                    ],
                    "metrics": [{"expression": f"ga:{x}"} for x in self._metrics],
                    "dimensions": [{"name": f"ga:{x}"} for x in self._dims],
                    "pageSize": size,
                    "pageToken": page_token,
                    "hideTotals": hide_totals,
                }
            ]
        }

        if self._dim_filter is not None:
            req_obj["reportRequests"][0]["dimensionFilterClauses"] = [
                {
                    "filters": [
                        {
                            "dimensionName": f"ga:{x[0]}",
                            "not": f"{x[1]}",
                            "operator": f"{x[2]}",
                            "expressions": f"{x[3]}",
                            "caseSensitive": f"{x[4]}",
                        }
                        for x in self._dim_filter
                    ]
                }
            ]
        if self._metric_filter is not None:
            req_obj["reportRequests"][0]["metricFilterClauses"] = [
                {
                    "filters": [
                        {
                            "metricName": f"ga:{x[0]}",
                            "not": f"{x[1]}",
                            "operator": f"{x[2]}",
                            "comparisonValue": f"{x[3]}",
                        }
                        for x in self._metric_filter
                    ]
                }
            ]

        if pull:
            return self.pull(req_obj)
        else:
            return req_obj

    def pull(self, request_body):
        """
        Parameters:
        request_body: structured request body for API call,
                       created by using self.build_request
          type: dict

        this function is often called right after
        `self.build_request()` being triggered by the
        pull=True parameter from the previous module

        returns the data in two options depending on how the
        class was initialized self.make_df is the variable
        that will change this return

        1) a created pd.DataFrame
        2) a raw response body (dictionary)
        """
        self.raw_data = self.auth.reports().batchGet(body=request_body).execute()
        if self.make_df:
            return self.create_df()
        else:
            return self.raw_data

    def create_df(self):
        """
        Loops through the Google Analytics batchGet()
        response json to create a pd.DataFrame

        Assigns variable types to columns
        """
        final_df = pd.DataFrame()
        for x in self.raw_data["reports"]:
            met = []
            cols = x.get("columnHeader")
            dims = cols["dimensions"]

            for header in cols["metricHeader"]["metricHeaderEntries"]:
                met.append(header.get("name"))

            row_data = x["data"].get("rows")
            metric_df = pd.DataFrame(
                [m["metrics"][0]["values"] for m in row_data], columns=met
            )

            # assign the variable types
            for col in cols["metricHeader"]["metricHeaderEntries"]:
                col_name = col.get("name")
                if col_name in metric_df.columns:
                    if col.get("type") in ["FLOAT", "PERCENT", "TIME", "CURRENCY"]:
                        metric_df[col_name] = metric_df[col_name].astype(float)
                    elif col.get("type") in ["INTEGER"]:
                        metric_df[col_name] = metric_df[col_name].astype(int)

            dim_df = pd.DataFrame([d["dimensions"] for d in row_data], columns=dims)
            metric_df.index.name = "idx"
            dim_df.index.name = "idx"
            df = dim_df.merge(metric_df, on="idx")
            df.columns = [x.replace("ga:", "") for x in df.columns]
            final_df = final_df.append(df)

        return final_df
