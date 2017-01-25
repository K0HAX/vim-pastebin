#!/usr/bin/env python3
import vim
import string
import urllib
import httplib2

buf = vim.current.buffer
text = '\n'.join(buf)

language = vim.eval("a:mLanguage")

params = urllib.parse.urlencode({'code': text, 'lng': language})
headers = {"Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"}

conn = httplib2.HTTPSConnectionWithTimeout('paste.k0hax.com', 443, ca_certs="/etc/ssl/certs/ca-bundle.crt")
conn.request("POST", "/send.php", params, headers)
response = conn.getresponse()
headers = dict(response.getheaders())

data = response.read()
print("Saved to: https://paste.k0hax.com/{}".format(headers['Location'].lstrip('./')))

conn.close()

