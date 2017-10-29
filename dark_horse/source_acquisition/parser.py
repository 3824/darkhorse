# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs, urljoin
import re
import json
from logging import getLogger, StreamHandler, DEBUG
import dark_horse.data.db_util as db_util

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

def parse(from_year, to_year, from_month, to_month, item_in_page =100, page=1):
    url_template = "http://www.jbis.or.jp/race/result/?sid=result&y_f={from_year}&m_f={from_month}&y_t={to_year}" \
          "&m_t={to_month}&coursec=coursec_01&coursec=coursec_02&coursec=coursec_03&coursec=coursec_04" \
          "&coursec=coursec_05&coursec=coursec_06&coursec=coursec_07&coursec=coursec_08" \
          "&coursec=coursec_09&coursec=coursec_10&items={item_in_page}&page={page}"

    init_url = url_template.format(from_year=from_year, to_year=to_year, from_month=from_month, to_month=to_month, item_in_page=item_in_page, page=page)

    logger.debug("initial URL: {}".format(init_url))

    result_count = parse_page(init_url)

    # 2ページ目以降（101〜200件 以降）を検索
    for i in range(int(result_count/item_in_page)):
        page = (i+2) # pageパラメータは1スタートなので
        url = url_template.format(from_year=from_year, to_year=to_year, from_month=from_month, to_month=to_month, item_in_page=item_in_page, page=page)
        logger.debug("parse URL: {}".format(url))
        parse_page(url)


def parse_page(url):
    """
    渡されたURLのページをパースするだけ
    :param url:
    :return:
    """
    response = urllib.request.urlopen(url)
    data = response.read()

    uri = urlparse(url)
    base_url = "{}://{}/".format(uri.scheme, uri.netloc)

    soup = BeautifulSoup(data, "html5lib")

    ### 検索結果の総数を取得しておく
    result_count = 0
    for count_desc in soup.find_all("p", class_="count"):
        if count_desc:
            print(count_desc)
            match = re.search(r"【(\d+)件中", count_desc.string)
            if match:
                result_count = int(match.group(1))

    header = []
    header_read = False
    maps = []
    for tr in soup.table.find_all("tr"):
        columns =  [x for x in tr.contents if x != "\n"]
        if (columns[1].name == "th") & (~header_read):
            for col in columns:
                try:
                    for child in col.descendants:
                        if child.name == "a":
                            header.append(child.string)
                            # header.append("{}_url".format(child.string))
                except:
                    pass
            header_read = True
        elif columns[1].name == "td":
            map = {}
            for index in range(len(columns)):
                col = columns[index]
                map[header[index]] = re.sub("\u3000", " ", str(col.string).strip())

                try:
                    for child in col.descendants:
                        if child.name == "a":
                            map["{}_url".format(header[index])] = urljoin(base_url, child.get("href"))
                except:
                    pass
            maps.append(map)

    print(maps[0].keys())
    print(maps[0])
    db_util.insert_search_result(maps)
    return result_count

if __name__ == '__main__':
    from_year = 2016
    to_year = 2016
    from_month = 11
    to_month = 11
    parse(from_year, to_year, from_month, to_month)

