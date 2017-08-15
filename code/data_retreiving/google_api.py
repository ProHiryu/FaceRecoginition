# -*-coding:utf8-*-

import requests
from get_names import get_name_list
import json

url = "https://www.googleapis.com/customsearch/v1"

querystring = {"q":"","cx":"your_cx","key":"your_key","startIndex":"1","searchType":"image"}

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'x-requested-with': "XMLHttpRequestAccept:text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'postman-token': "60904456-08be-5a31-ecd2-e818e5fb0d01"
    }


def get_image():
    names = get_name_list()
    for name in names:
        querystring['q'] = name
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.content)
        print(searchUrl)
        print(r)
        print(result)



if __name__ == "__main__":
    get_image()
