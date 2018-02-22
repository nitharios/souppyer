from bs4 import BeautifulSoup as soup
from urllib.request import FancyURLopener, urlopen
from urllib.error import HTTPError

# comment out or program will break
from lib import script
from assets.config import url, path

try:
  class AppURLopener(FancyURLopener):
    version = "Mozilla/5.0"
  opener = AppURLopener()
  response = opener.open(url)

except HTTPError as e:
  print(e)

else:
  # append & interpret binary
  f = open(path, 'ab')
  data = response.read()
  f.write(data)
  f.close

# comment out or program will break
print(script.run())