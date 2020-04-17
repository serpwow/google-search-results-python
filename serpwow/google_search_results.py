import requests
import json

class GoogleSearchResults(object):
    """GoogleSearchResults allows you to interact with the SerpWow API to search Google and return parsed JSON, HTML or CSV data. You can also access the SerpWow Locations and Account utility APIs.
    ```python
    from google_search_results import GoogleSearchResults

    serpwow = GoogleSearchResults("API_KEY")

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
    ENDPOINT_BATCHES = "http://localhost/live/batches"

    def __init__(self, api_key):
        self.API_KEY = api_key


    def http_get(self, params_dict, prefix, isJson=True):
        try:

            if params_dict:
                self.params_dict = params_dict
            else:
                self.params_dict = {}

            self.params_dict["source"] = "python"
            self.params_dict["api_key"] = self.API_KEY

            response = requests.get(prefix, self.params_dict, timeout=600)
            
            if isJson:
                return response.content
            else:
                return response.text

        except requests.HTTPError as e:
            print(e, e.response.status_code)

    def http_post(self, payload, prefix):
        try:

            if payload:
                self.payload = payload
            else:
                self.payload = {}

            self.payload["source"] = "python"

            url = prefix + "?app_name=serpwow&api_key=" + self.API_KEY

            headers = {'Content-type': 'application/json' }
            response = requests.post(url, json=self.payload, timeout=600, headers=headers)

            return response.text

        except requests.HTTPError as e:
            print(e, e.response.status_code)

    def http_put(self, payload, prefix):
        try:

            if payload:
                self.payload = payload
            else:
                self.payload = {}

            self.payload["source"] = "python"

            url = prefix + "?api_key=" + self.API_KEY

            headers = {'Content-type': 'application/json' }
            response = requests.put(url, json=self.payload, timeout=600, headers=headers)

            return response.text

        except requests.HTTPError as e:
            print(e, e.response.status_code)

    def http_delete(self, url):
        try:

            url = url + "?api_key=" + self.API_KEY + "&source=python"

            response = requests.delete(url, timeout=600)

            return response.text

        except requests.HTTPError as e:
            print(e, e.response.status_code)


    def get_json(self, params):
        """Returns:
            JSON with the formatted response content
        """
        params["output"] = "json"
        return json.loads(self.http_get(params, self.ENDPOINT_SEARCH, True).decode('utf-8'))

    def get_html(self, params):
        """Returns:
            HTML with the formatted response content
        """
        params["output"] = "html"
        return self.http_get(params, self.ENDPOINT_SEARCH, False)

    def get_csv(self, params):
        """Returns:
            CSV with the formatted response content
        """
        params["output"] = "csv"
        return self.http_get(params, self.ENDPOINT_SEARCH, False)


    def get_locations(self, params):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get(params, self.ENDPOINT_LOCATIONS, True))


    def get_account(self):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get(None, self.ENDPOINT_ACCOUNT, True))


    def create_batch(self, params):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_post(params, self.ENDPOINT_BATCHES))
    
    def update_batch(self, batch_id, params):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_put(params, self.ENDPOINT_BATCHES + "/" + str(batch_id)))

    def start_batch(self, batch_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/start", True))

    def stop_batch(self, batch_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/stop", True))

    def get_batch(self, batch_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES + "/" + str(batch_id), True))

    def list_batches(self):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES, True))

    def delete_batch(self, batch_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_delete(self.ENDPOINT_BATCHES + "/" + str(batch_id)))

    def update_batch_search(self, batch_id, search_id, params):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_put(params, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/" + str(search_id)))

    def delete_batch_search(self, batch_id, search_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_delete(self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/" + str(search_id)))

    def list_batch_searches(self, batch_id, page):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/searches/" + str(page), True))

    def find_batch_searches(self, batch_id, page, searchTerm):
        """Returns:
            JSON with the formatted response content
        """
        params = {}
        params["q"] = searchTerm
        return json.loads(self.http_get(params, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/searches/" + str(page), True))

    def list_batch_searches_as_json(self, batch_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/searches/json", True))

    def list_batch_searches_as_csv(self, batch_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/searches/csv", False))

    def list_batch_result_sets(self, batch_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/results", True))

    def get_batch_result_set(self, batch_id, result_set_id):
        """Returns:
            JSON with the formatted response content
        """
        return json.loads(self.http_get({}, self.ENDPOINT_BATCHES + "/" + str(batch_id) + "/results/" + str(result_set_id), True))

