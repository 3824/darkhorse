## レース一覧ページのURLから各レースの詳細ページURLリストを取得する。
from time import sleep
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urljoin
import glob, os, tqdm

from model.race_url import RaceUrl
from model.setting import session

base_url = "https://db.netkeiba.com"

def load_detail_page(summary_url):
    response = request.urlopen(summary_url)
    bs = BeautifulSoup(response, "html.parser")

    result = set()
    for table in bs.find_all("table", class_="race_table_01 nk_tb_common"):
        for ref in table.select("a"):
            if ref.get("href").startswith("/race"):
                u = urljoin(base_url, ref.get("href"))
                result.add(u)
                ru = RaceUrl()
                ru.summary_url = summary_url
                ru.race_url = u
                session.merge(ru)
                session.commit()
    return result

def load_retrieved_urls():
    summary_urls = session.query(RaceUrl.summary_url).all()
    return [u.summary_url for u in summary_urls]

def read_files(summary_dir):
    urls = set()
    print(os.path.join(summary_dir, "*"))
    for file in glob.glob(os.path.join(summary_dir, "*")):
        with open(file, "r") as f:
            for line in f:
                if line is not None and line.strip() != "":
                    urls.add(line.strip())
    return list(urls)

def retrieve_race_pages(summary_dir, max_races=10):
    """_summary_

    Args:
        summary_dir (_type_): path of summary directory
        max_races (int, optional): max race page urls which retrieve at once. Defaults to 10.
    """
    summary_urls = load_retrieved_urls()

    urls = read_files(summary_dir)
    urls = list(set(urls) - set(summary_urls))

    print(len(urls))
    for i in tqdm.tqdm(range(0, len(urls))):
        if i > max_races:
            break
        load_detail_page(urls[i])
        sleep(1)

if __name__ == '__main__':
    summary_dir = "./dark_horse/summary"
    # url = "https://db.netkeiba.com/race/sum/42/20220809/"
    # res = load_detail_page(url)
    # print(res)

    retrieve_race_pages(summary_dir, 5)
