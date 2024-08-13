#!/usr/bin/python3

"""
Network problem-> DNS Failure, refused connection:
    ConnectionError Exception will be raised by requests.

Response.raise_for_status() -> HTTP Error if the HTTP request returned an unsuccessful status code.

Timeout Exception -> if a request times out.

If a request exceeds the configured number of maximum redirections, a TooManyRedirects Exception is raised.

All exceptions that requests explicitly raises inherit from requests.exceptions.RequestException.
"""
