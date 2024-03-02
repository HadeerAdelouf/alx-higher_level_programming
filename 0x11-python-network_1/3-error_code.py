#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    uRl = sys.argv[1]

    _request = request.Request(uRl)
    try:
        with request.urlopen(_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as E:
        print("Error code: {}".format(E.code))
