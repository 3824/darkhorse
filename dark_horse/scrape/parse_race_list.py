## 日付入力してlistページからrace_idの一覧を取得する。
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urljoin


def load_list(date_str):
    url = f"https://db.netkeiba.com/?pid=race_kaisai&date={date_str}"
    print(url)
    response = request.urlopen(url)
    bs = BeautifulSoup(response, "html.parser")
    for item in bs.find_all("dl", class_="race_top_data_info fc"):
        print(urljoin(url, item.select("a")[0].get('href')))

if __name__ == '__main__':
    load_list("20210306")