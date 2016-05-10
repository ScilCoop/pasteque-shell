import requests


# This is the requests wrapper.
# It hold an Api class which is called to get the url: api.url, api.data
# api.data is a dictionnary which is what requests use
# http://docs.python-requests.org/en/master/
class Request:
    api = None

    def __init__(self, api):
        self.api = api

    def get(self):
        return requests.get(self.api.url(), params=self.api.data)
