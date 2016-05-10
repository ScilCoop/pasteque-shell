#!/usr/bin/python

# Requests is the less verbose http package in the official python libs.
# We should not have to use urllib2 or urllib3
import requests

from Pasteque import Request
from api.CashRegistersApi import CashRegistersApi

# Create the API module which is automatically set from the configuration file
# LOGIN / PASSWORD / HOSTNAME /
api = CashRegistersApi()

# Set the API action to: getAll => api.php?p=getAll
api.getAll()

# Request.get create and send the request from the given api module
request = Request(api).get()

# you can print the request result
print(request.json())
