# -*-coding:utf8-*-

import requests
from get_names import get_name_list

key = "AIzaSyDDC5orS4QQiXcKbQSU60kDgQ_VOML-2bc"

def get_image():
    names = get_name_list()
    for name in names:
        re = url_open(url,name)
