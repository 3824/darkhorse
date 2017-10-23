from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs
import re

def parse():
    url = """
    http://www.jbis.or.jp/race/result/?sid=result&y_f=2016&m_f=11&y_t=2016&m_t=11&coursec=coursec_01&coursec=coursec_02&coursec=coursec_03&coursec=coursec_04&coursec=coursec_05&coursec=coursec_06&coursec=coursec_07&coursec=coursec_08&coursec=coursec_09&coursec=coursec_10&items=100
    """
    response = urllib.request.urlopen(url)
    data = response.read()

    base_url = urlparse(url)._replace(query=None).geturl()
    print(base_url)

    soup = BeautifulSoup(data, "html5lib")

    header = []
    header_read = False
    rows = []
    for tr in soup.table.find_all("tr"):
        columns =  [x for x in tr.contents if x != "\n"]
        if (columns[1].name == "th") & (~header_read):
            for col in columns:
                try:
                    for child in col.descendants:
                        if child.name == "a":
                            header.append(child.string)
                            header.append("{}_url".format(child.string))
                except:
                    pass
            header_read = True
        elif columns[1].name == "td":
            # row = [re.sub("\u3000", " ", str(col.string).strip()) for col in columns]
            row = []
            for col in columns:
                row.append(re.sub("\u3000", " ", str(col.string).strip()))
                try:
                    for child in col.descendants:
                        if child.name == "a":
                            row.append(child.get("href"))
                except:
                    pass
            rows.append(row)

    print(header)
    print(rows[0])
    print(rows[1])
    print(rows[2])
    print(rows[3])

if __name__ == '__main__':
    parse()

