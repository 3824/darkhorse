from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs, urljoin
import re
import json

def parse_jockey_history(url):
    response = urllib.request.urlopen(url+"?items=100")
    data = response.read()

    uri = urlparse(url)
    base_url = "{}://{}/".format(uri.scheme, uri.netloc)

    soup = BeautifulSoup(data, "html5lib")

    header = []
    header_read = False
    maps = []
    for tr in soup.table.find_all("tr"):
        columns =  [x for x in tr.contents if x != "\n"]
        if (columns[1].name == "th") & (~header_read):
            for col in columns:
                try:
                    for child in col.descendants:
                        if child.name == "a":
                            header.append(child.string)
                            # header.append("{}_url".format(child.string))
                except:
                    pass
            header_read = True
        elif columns[1].name == "td":
            map = {}
            index = 0
            for col in columns:
                has_li = False
                for child in col.descendants:
                    if child.name == "li":
                        has_li = True
                        break
                if has_li:
                    continue
                map[header[index]] = re.sub("\u3000", " ", str(col.string).strip())

                try:
                    for child in col.descendants:
                        if child.name == "a":
                            map["{}_url".format(header[index])] = urljoin(base_url, child.get("href"))
                except:
                    pass
                index += 1
            maps.append(map)

    print(header)
    print(maps[0])

if __name__ == '__main__':
    url = "http://www.jbis.or.jp/race/jockey/J00655/"
    parse_jockey_history(url)
