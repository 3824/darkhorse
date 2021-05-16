from bs4 import BeautifulSoup
from urllib import request
import re


def parse_horse_page(url):
    response = request.urlopen(url)
    bs = BeautifulSoup(response, "html.parser")
    name = bs.select("title")[0].text.split("|")[0].strip()
    tb = bs.find_all("table", class_="db_prof_table no_OwnerUnit")[0]
    for tr in tb.findAll("tr"):
        th_text = tr.select("th")[0].text
        val = tr.select("td")[0].text
        if th_text == "生年月日":
            birth = val
        elif th_text == "調教師":
            trainer = val
        elif th_text =="馬主":
            owner = val
        elif th_text =="生産者":
            breeder = val
        elif th_text =="産地":
            hometown = val
        elif th_text =="セリ取引価格":
            price = val

    print("{} ({}) {}".format(name, birth, price))

## サンプルURL
# https://db.netkeiba.com/horse/2018106461/
if __name__ == '__main__':
    url = "https://db.netkeiba.com/horse/2018106461/"
    parse_horse_page(url)
