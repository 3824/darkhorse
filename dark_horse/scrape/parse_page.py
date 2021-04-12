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

def parse_page(id):
    url = f"https://db.netkeiba.com/race/{id}/"
    response = request.urlopen(url)
    bs = BeautifulSoup(response, "html.parser")
    print(bs.select("span"))

    race_type = bs.select("span")[6].text
    print(race_type)

    race_type = load_race_type(race_type)
    print(race_type)

if __name__ == '__main__':
    parse_page("202143040901")
