"""
30. Write a Python program to access and print a URL's content to the console.
"""
# Solved by Zeeshan Sarwar

import requests

"""
get(url, params=None, **kwargs)
    Sends a GET request.
    
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
"""
data = requests.get('https://www.medium.com/')
# print(data.text)

print(data.text)    # display Content of the response, in unicode.


# print(help(requests.get))