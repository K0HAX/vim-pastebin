#!/usr/bin/python
import vim
import string
import urllib
import httplib

text = string.join(vim.current.buffer, "\n")

language = vim.eval("a:mLanguage")

params = urllib.urlencode({'code': text, 'lng': language})
headers = {"Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"}

conn = httplib.HTTPSConnection('paste.k0hax.com', 443)
conn.request("POST", "/send.php", params, headers)
response = conn.getresponse()
headers = dict(response.getheaders())

data = response.read()
print("Saved to: https://paste.k0hax.com/" + headers['location'].lstrip('./'))

conn.close()

