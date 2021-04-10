from bs4 import BeautifulSoup
from urllib import request

def parse_page(id):
    url = f"https://db.netkeiba.com/race/{id}/"
    response = request.urlopen(url)
    bs = BeautifulSoup(response, "html.parser")
    print(bs.select("span"))

if __name__ == '__main__':
    parse_page("202143040901")