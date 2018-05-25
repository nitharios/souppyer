import csv
import requests as req

from bs4 import BeautifulSoup as soup
from assets.config import url, path_to_file
from lib import script   # comment out or program will break

def program():
  # scrape data
  data = req.get('https://medium.com/topic/technology')
  # parse data
  data = soup(data.text, 'html.parser')  # have to use a parser or data will be unreadable
  # find all that matches a case and store as list
  data = data.find_all('a', class_='')
  # slice notation -> list[start_index:end_index:step]
  # necessary because of repeating links in scraped code
  data = data[::2]
  # loop through list
  for key in data:
    # grab link by key 'href'
    link = key['href']
    # find string index of '?'
    slice_index = link.find('?')
    # slice the link at the index of '?'
    link = link[:slice_index]

    # open file and write to it
    with open(path_to_file, 'a') as file:
      writer = csv.writer(file)
      writer.writerow([link])

  print(script.engage())  # comment out or program will break

script.start(program)
