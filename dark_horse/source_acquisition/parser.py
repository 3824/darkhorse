from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs, urljoin
import re
import json

def parse():
    url = "http://www.jbis.or.jp/race/result/?sid=result&y_f=2016&m_f=11&y_t=2016&m_t=11&coursec=coursec_01&coursec=coursec_02&coursec=coursec_03&coursec=coursec_04&coursec=coursec_05&coursec=coursec_06&coursec=coursec_07&coursec=coursec_08&coursec=coursec_09&coursec=coursec_10&items=100"
    response = urllib.request.urlopen(url)
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
            for index in range(len(columns)):
                col = columns[index]
                map[header[index]] = re.sub("\u3000", " ", str(col.string).strip())

                try:
                    for child in col.descendants:
                        if child.name == "a":
                            map["{}_url".format(header[index])] = urljoin(base_url, child.get("href"))
                except:
                    pass
            maps.append(map)

    print(header)
    print(maps[0])

if __name__ == '__main__':
    parse()

