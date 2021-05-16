import glob

from dark_horse.scrape.parse_each_day_race import load_detail_page
from dark_horse.scrape.parse_page import parse_page_url


def get_detail(summary_url):
    print("summary: {}".format(summary_url))
    detail_url_list = load_detail_page(summary_url)
    for detail_url in detail_url_list:
        print(detail_url)
        parse_page_url(detail_url) # レース情報ととりあえず一着のみ抽出して表示してる。
        # 詳細ページには、馬リンクと騎手リンクがあるので抽出したい→マスター情報＋戦績になる??
        return
        # TODO parse_page_urlにて詳細ページから取得する情報のデータ形式きめる。

if __name__ == '__main__':
    summay_dir = "../summary/*.txt"

    files = []
    for file in glob.glob(summay_dir):
        print(file)
        with open(file, mode="r") as f:
            files = f.readlines()
    get_detail(files[0])
