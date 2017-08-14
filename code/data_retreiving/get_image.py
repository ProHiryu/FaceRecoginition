# -*-coding:utf8-*-

import requests
from get_names import get_name_list

# http://image.baidu.com/data/imgs?col=&tag=&sort=&pn=&rn=&p=channel&from=1
# 参数：col=大类&tag=分类&sort=0&pn=开始条数&rn=显示数量&p=channel&from=1

url = "http://image.baidu.com/data/imgs?rn=50&word="

def get_image():
    names = get_name_list()
    for name in names[1:3]:
        url_tmp = url + name
        re = requests.get(url_tmp)
        print(re.content)


if __name__ == "__main__":
    get_image()
