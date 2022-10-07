## 日付入力してlistページからrace_idの一覧を取得する。
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urljoin

base_url = "https://db.netkeiba.com"

def load_list_each_day(date_str):
    url = f"https://db.netkeiba.com/?pid=race_kaisai&date={date_str}"
    response = request.urlopen(url)
    bs = BeautifulSoup(response, "html.parser")
    # for item in bs.find_all("dl", class_="race_top_data_info fc"):
    #     print(urljoin(url, item.select("a")[0].get('href')))
    central_pages = [urljoin(base_url, item.select("a")[0].get('href')) for item in bs.find_all("dl", class_="race_top_data_info fc")]

    # 中央と地方競馬の結果を取得したい
    result = set()
    races = bs.find_all("div", class_="race_kaisai")
    for race in races:
        for dd in race.select("dd"):
            for ref in dd.select("a"):
                if ref.text == "一覧":
                    result.add(urljoin(base_url, ref.get("href")))
    return result

def load_list(day_list):
    result = set()
    for day_str in day_list:
        result = result.union(load_list_each_day(day_str))
    return result

if __name__ == '__main__':
    # print(load_list(["20210306", "20210305","20210304","20210303","20210302"]))
    print(load_list(["20210306"]))
