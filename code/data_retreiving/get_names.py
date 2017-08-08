#-*-coding:utf8-*-

from bs4 import BeautifulSoup
import requests

url = "https://zh.wikipedia.org/wiki/AV%E5%A5%B3%E5%84%AA%E5%88%97%E8%A1%A8#2016.E5.B9.B4.E5.87.BA.E9.81.93_AV.E5.A5.B3.E5.84.AA.E5.88.97.E8.A1.A8"

r = requests.get(url)

soup = BeautifulSoup(r,"html.parser")

print(soup)
