from bs4 import BeautifulSoup as soup
from urllib.request import FancyURLopener, urlopen
from urllib.error import HTTPError

from lib import script   # comment out or program will break
from assets.config import url, path

try:
  class AppURLopener(FancyURLopener):
    # required to mimic a browser
    version = "Mozilla/5.0"
  opener = AppURLopener()
  response = opener.open(url)

except HTTPError as e:
  print(e)

else:
  f = open(path, 'ab')    # append & interpret binary
  data = response.read()
  f.write(data)
  f.close

print(script.run())  # comment out or program will break