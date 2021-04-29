## 日付入力してlistページからrace_idの一覧を取得する。
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urljoin

base_url = "https://db.netkeiba.com"

def load_list(date_str):
    url = f"https://db.netkeiba.com/?pid=race_kaisai&date={date_str}"
    print(url)
    response = request.urlopen(url)
    bs = BeautifulSoup(response, "html.parser")
    # for item in bs.find_all("dl", class_="race_top_data_info fc"):
    #     print(urljoin(url, item.select("a")[0].get('href')))
    central_pages = [urljoin(base_url, item.select("a")[0].get('href')) for item in bs.find_all("dl", class_="race_top_data_info fc")]

    # 地方競馬の結果を取得したい
    
    return central_pages

if __name__ == '__main__':
    print(load_list("20210306"))
    print(load_list("20210305"))
