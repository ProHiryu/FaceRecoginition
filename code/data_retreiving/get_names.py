#-*-coding:utf8-*-

from bs4 import BeautifulSoup
import requests


def get_name_list():
    url = "http://www.ttpaihang.com/vote/rank.php?voteid=1089"
    page = "&page="

    Name_List = []

    for i in range(5):
        i += 1
        i = str(i)
        page_use = page + i
        url_use = url + page_use

        r = requests.get(url_use)
        r.encoding = 'gbk'

        if r.status_code == 200:
            soup = BeautifulSoup(r.text,"html.parser")
        else:
            print("requests error")

        ztheis = soup.find_all('td',class_ = "zthei")

        for zthei in ztheis:
            if zthei.find_all("a") != []:
                a = zthei.find("a")
                Name_List.append(a.contents[0])

    return Name_List

if __name__ == "__main__":
    r = get_name_list()
    print(r)
