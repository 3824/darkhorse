from bs4 import BeautifulSoup
from urllib import request
import re
from dark_horse.model.horse import Horse
from dark_horse.model.setting import session

price_pattern = re.compile(r"([\d,億]+)万円")

def extract_price(price_str):
    m = price_pattern.match(price_str.strip())
    if m:
        return m.groups()[0].replace(",", "").replace("億", "")

def extract_id(url):
    match = re.search("horse/(.+)", url)
    if match:
        return match.group(1).replace("/", "")
    return ""

def parse_horse_page(url):
    h = Horse()

    h.id = extract_id(url)

    response = request.urlopen(url)
    bs = BeautifulSoup(response, "html.parser")
    h.name = bs.select("title")[0].text.split("|")[0].strip()

    # tb = bs.find_all("table", class_="db_prof_table no_OwnerUnit")[0]
    tb = bs.find_all("table", class_="db_prof_table")[0]
    for tr in tb.findAll("tr"):
        th_text = tr.select("th")[0].text
        val = tr.select("td")[0].text
        if th_text == "生年月日":
            h.birth = val
        elif th_text == "調教師":
            h.trainer = val
        elif th_text =="馬主":
            h.owner = val
        elif th_text =="生産者":
            h.breeder = val
        elif th_text =="産地":
            h.hometown = val
        elif th_text =="セリ取引価格":
            h.price = extract_price(val)
        elif th_text == "獲得賞金":
            h.get_price = extract_price(val)

    print(h)
    session.merge(h)
    session.commit()

## サンプルURL
# https://db.netkeiba.com/horse/2018106461/
if __name__ == '__main__':
    url = "https://db.netkeiba.com/horse/2018106461/"
    url = "https://db.netkeiba.com/horse/1992102988/"
    url = "https://db.netkeiba.com/horse/2017101010/"
    url = "https://db.netkeiba.com/horse/2019105498/"
    url = "https://db.netkeiba.com/horse/2018105204/"
    url = "https://db.netkeiba.com/horse/2016104163/"
    url = "https://db.netkeiba.com/horse/2016104750/"
    # url = "https://db.netkeiba.com/horse/2018104803/"
    parse_horse_page(url)
