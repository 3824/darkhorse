## レース一覧ページのURLから各レースの詳細ページURLリストを取得する。
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urljoin

base_url = "https://db.netkeiba.com"

def load_detail_page(summary_url):
    response = request.urlopen(summary_url)
    bs = BeautifulSoup(response, "html.parser")

    result = set()
    for table in bs.find_all("table", class_="race_table_01 nk_tb_common"):
        for ref in table.select("a"):
            if ref.get("href").startswith("/race"):
                result.add(urljoin(base_url, ref.get("href")))
    return result

if __name__ == '__main__':
    url = "https://db.netkeiba.com/race/sum/55/20210306/"
    res = load_detail_page(url)
    print(res)