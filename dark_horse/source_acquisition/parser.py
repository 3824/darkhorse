from bs4 import BeautifulSoup
import urllib.request

def parse():
    url = """
    http://www.jbis.or.jp/race/result/?sid=result&y_f=2016&m_f=11&y_t=2016&m_t=11&coursec=coursec_01&coursec=coursec_02&coursec=coursec_03&coursec=coursec_04&coursec=coursec_05&coursec=coursec_06&coursec=coursec_07&coursec=coursec_08&coursec=coursec_09&coursec=coursec_10&items=100
    """
    response = urllib.request.urlopen(url)
    data = response.read()

    soup = BeautifulSoup(data)

    print(str(soup))


if __name__ == '__main__':
    parse()

