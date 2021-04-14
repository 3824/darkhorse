from bs4 import BeautifulSoup
from urllib import request
import re

track_pattern = re.compile(r"(.)(.)(\d+)m")

class RaceType():
    def __init__(self, cource_info, weather, condition):
        self.cource = cource_info[0]
        self.direction = cource_info[1]
        self.distance = cource_info[2]
        self.weather = weather
        self.condition = condition

    def __str__(self):
        return "{}, {}, {} ({}, {})".format(self.cource, self.direction, self.distance, self.weather, self.condition)


def load_race_type(race_type_str):
    types = race_type_str.split("/")
    m = track_pattern.match(types[0].strip())
    if m:
        print(m.groups())
        race_type = RaceType(m.groups(), types[1].split(":")[1].strip(), types[2].split(":")[1].strip())
        return race_type
    else:
        return None

def load_each_result(tr):
    td_list = tr.find_all_next("td")
    rank = td_list[0].text
    frame_number =td_list[1].text
    horse_number = td_list[2].text
    horse_name = td_list[3].text.strip()
    jockey_name = td_list[6].text.strip()

    return rank, frame_number, horse_number, horse_name, jockey_name

def parse_page(id):
    url = f"https://db.netkeiba.com/race/{id}/"
    response = request.urlopen(url)
    bs = BeautifulSoup(response, "html.parser")
    print(bs.select("span"))

    race_type_str = bs.select("span")[6].text
    if race_type_str == "LIVE":
        race_type_str = bs.select("span")[7].text

    race_type = load_race_type(race_type_str)
    print(race_type)

    for tr in bs.find_all("tr"):
        if "class" in tr.attrs:
            continue
        print(load_each_result(tr))
        break
        ## <td>区切りで着順の情報が入っている。

if __name__ == '__main__':
    parse_page("202109010611")
