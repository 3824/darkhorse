from bs4 import BeautifulSoup
from urllib import request
import re

track_pattern = re.compile(r"(.)(.)(\d+)m")
gender_pattern = re.compile(r"^(.)(\d+)$")
time_pattern = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
weight_pattern = re.compile(r"^(\d+)\(([+-]\d+)\)$")
trainer_pattern = re.compile(r"^\[(.+)\]\s?(.+)$")


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


class HorseResult():
    def __init__(self, horse_id, horse_name, frame_number, horse_number, horse_gender, horse_age, time, diff, weight,
                 weight_diff, trainer_stable, trainer_name):
        self.horse_id = horse_id
        self.horse_name = horse_name
        self.frame_number = frame_number
        self.horse_number = horse_number
        self.horse_gender = horse_gender
        self.horse_age = horse_age
        self.time = time
        self.diff = diff
        self.weight = weight
        self.weight_diff = weight_diff
        self.trainer_stable = trainer_stable
        self.trainer_name = trainer_name

    def __str__(self):
        return "{}:{} ({}, {}), {}-{}, {}({}), ([{}] {})".format(self.horse_id, self.horse_name, self.frame_number, self.horse_number,
                                                              self.horse_gender,
                                                              self.horse_age, self.weight, self.weight_diff,
                                                              self.trainer_stable, self.trainer_name)


def load_each_result(tr):
    td_list = tr.find_all_next("td")
    rank = td_list[0].text
    frame_number = td_list[1].text
    horse_number = td_list[2].text
    horse_name = td_list[3].text.strip()
    horse_id =  td_list[3].find("a").get("href").replace("horse", "").replace("/", "")
    print("horse_id={}".format(horse_id))
    gm = gender_pattern.match(td_list[4].text.strip())
    if gm:
        horse_gender = gm.groups()[0]
        horse_age = gm.groups()[1]
    else:
        horse_gender = None
        horse_age = None
    jockey_weight = int(td_list[5].text.strip())
    jockey_name = td_list[6].text.strip()

    tm = time_pattern.match(td_list[7].text.strip())
    if tm:
        min = int(tm.groups()[0])
        sec = int(tm.groups()[1])
        milli = int(tm.groups()[2])
        time = min * 60 + sec + 0.1 * milli
    else:
        time = None
    diff = td_list[8].text.strip()

    ## 馬体重
    wm = weight_pattern.match(td_list[14].text.strip())
    if wm:
        horse_weight = int(wm.groups()[0])
        horse_weight_diff = wm.groups()[1]
    else:
        horse_weight = None
        horse_weight_diff = None

    ## 調教師
    tm = trainer_pattern.match(td_list[18].text.strip())
    if tm:
        trainer_stable = tm.groups()[0]
        trainer_name = tm.groups()[1]
    else:
        trainer_stable = None
        trainer_name = None

    hr = HorseResult(horse_id, horse_name, frame_number, horse_number, horse_gender, horse_age, time, diff, horse_weight,
                     horse_weight_diff, trainer_stable, trainer_name)

    return rank, frame_number, horse_number, horse_name, jockey_name, hr

def parse_page(race_id):
    url = f"https://db.netkeiba.com/race/{race_id}/"
    return parse_page_url(url)

def parse_page_url(url):
    print("parse page: {}".format(url))
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
        each_result = load_each_result(tr)

        print(each_result)
        print(each_result[-1])
        break # とりあえず一着のみ
        ## <td>区切りで着順の情報が入っている。


if __name__ == '__main__':
    parse_page("202109010611")
