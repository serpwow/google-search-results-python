import requests
import json

class GoogleSearchResults(object):
    """GoogleSearchResults allows you to interact with the SerpWow API to search Google and return parsed JSON, HTML or CSV data. You can also access the SerpWow Locations and Account utility APIs.
    ```python
    from google_search_results import GoogleSearchResults

    serpwow = GoogleSearchResults("demo")

    params = {
    "q" : "pizza",
    "location" : "New York,New York,United States"
    }

    result = serpwow.get_json(params)

    print result
    ```
    https://github.com/serpwow/google-search-results-python
    """

    API_KEY = None
    ENDPOINT_SEARCH = "https://api.serpwow.com/live/search"
    ENDPOINT_LOCATIONS = "https://api.serpwow.com/live/locations"
    ENDPOINT_ACCOUNT = "https://api.serpwow.com/live/account"

    def __init__(self, api_key):
        self.API_KEY = api_key

    def get_results(self, params_dict, prefix):
        try:

            if params_dict:
                self.params_dict = params_dict
            else:
                self.params_dict = {}

            self.params_dict["source"] = "python"
            self.params_dict["api_key"] = self.API_KEY

            response = requests.get(prefix, self.params_dict, timeout=600)

            return response.text

        except requests.HTTPError as e:
            print(e, e.response.status_code)

    def get_json(self, params):
        """Returns:
            JSON with the formatted response content
        """
        params["output"] = "json"
        return json.loads(self.get_results(params, self.ENDPOINT_SEARCH))

    def get_html(self, params):
        """Returns:
            HTML with the formatted response content
        """
        params["output"] = "html"
        return self.get_results(params, self.ENDPOINT_SEARCH)

    def get_csv(self, params):
        """Returns:
            CSV with the formatted response content
        """
        params["output"] = "csv"
        return self.get_results(params, self.ENDPOINT_SEARCH)

    def get_locations(self, params):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.get_results(params, self.ENDPOINT_LOCATIONS))

    def get_account(self):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.get_results(None, self.ENDPOINT_ACCOUNT))