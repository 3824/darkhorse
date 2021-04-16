from bs4 import BeautifulSoup
from urllib import request
import re

track_pattern = re.compile(r"(.)(.)(\d+)m")
gender_pattern = re.compile(r"^(.)(\d+)$")
time_pattern = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")

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
    def __init__(self, horse_name, frame_number, horse_number, horse_gender, horse_age, time, diff):
        self.horse_name = horse_name
        self.frame_number = frame_number
        self.horse_number = horse_number
        self.horse_gender = horse_gender
        self.horse_age = horse_age
        self.time = time
        self.diff = diff

    def __str__(self):
        return "{} ({}, {}), {}-{}".format(self.horse_name, self.frame_number, self.horse_number, self.horse_gender, self.horse_age)

def load_each_result(tr):
    td_list = tr.find_all_next("td")
    rank = td_list[0].text
    frame_number =td_list[1].text
    horse_number = td_list[2].text
    horse_name = td_list[3].text.strip()
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
        time = min*60 + sec + 0.1*milli
    else:
        time = None
    diff = td_list[8].text.strip()

    hr = HorseResult(horse_name, frame_number, horse_number, horse_gender, horse_age, time, diff)

    return rank, frame_number, horse_number, horse_name, jockey_name, hr

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
        each_result = load_each_result(tr)

        print(each_result)
        print(each_result[-1])
        break
        ## <td>区切りで着順の情報が入っている。

if __name__ == '__main__':
    parse_page("202109010611")
