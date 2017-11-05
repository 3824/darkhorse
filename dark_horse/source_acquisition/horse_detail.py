from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs, urljoin
import re
import dark_horse.data.db_util as db_util

def parse_horse_basic(url):
    pass

if __name__ == '__main__':
    url = "http://www.jbis.or.jp/horse/0001152929/"
    parse_horse_basic(url)
