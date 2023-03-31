import requests
import favicon
from sys import argv
import os
from urllib.parse import urlparse

file_path = '/tmp/favicons'

if not os.path.exists(file_path):
  try:
    os.mkdir(file_path)
  except OSError as err:
    print(err)

script, url = argv

domain = urlparse(url).netloc

icons = favicon.get(url)
icon = icons[0]

response = requests.get(icon.url, stream=True)
with open('/tmp/favicons/'+ domain +'.{}'.format(icon.format), 'wb') as image:
    for chunk in response.iter_content(1024):
        image.write(chunk)
