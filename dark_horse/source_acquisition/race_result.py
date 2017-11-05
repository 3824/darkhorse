from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs, urljoin
import re
import dark_horse.data.db_util as db_util

def parse_race_result(url):
    response = urllib.request.urlopen(url+"?items=100")
    data = response.read()

    uri = urlparse(url)
    base_url = "{}://{}/".format(uri.scheme, uri.netloc)

    soup = BeautifulSoup(data, "html5lib")
    race_name = soup.find_all("h2", class_="hdg-l2-06")#, attr={"class": "hdg-l2-06"})[0].text

    cond = soup.find_all("ul", class_="list-inline-02 reset-mb-00")[0]
    items = [x for x in cond.contents if x != "\n"]
    race_type = items[0].text
    weather = items[1].text
    soil = items[2].text

    prize_block = soup.find_all("ul", class_="list-inline-01")[0]
    prizes = [x.text for x in prize_block.contents if x != "\n"]


    race_details = soup.find_all("table", class_="tbl-data-04")[0]
    column_list = []
    maps = []
    for table_block in [item for item in race_details.contents if item != "\n"]:
        if table_block.name == "thead":
            for child in table_block.descendants:
                if child.name == "th":
                    column_list.append(child.text)
        elif table_block.name == "tbody":
            for row in table_block.children:
                if row.name != "tr":
                    continue
                index = 0
                map = {}
                for child in row.children:
                    if (child.name == "th") | (child.name == "td"):
                        print("{}: {}".format(column_list[index], child.text))
                        map[column_list[index]] = child.text
                        for tag in child.children:
                            if tag.name == "a":
                                map["{}_url".format(column_list[index])] = urljoin(base_url, tag.get("href"))
                        index += 1
                maps.append(map)
        db_util.insert_race_result(maps)

if __name__ == '__main__':
    url = "http://www.jbis.or.jp/race/result/20161120/103/04/"
    parse_race_result(url)
