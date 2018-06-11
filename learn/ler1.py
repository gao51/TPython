import urllib.request as urllib
from urllib import request

import requests as requests
import time
import urllib3


def linkbaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib.urlopen(url,timeout=3)
        print(response.info())
    except urllib.URLError:
        print("地址错误")
        exit()
    with open('./baidu.txt','w') as fp:
        fp.write(str(response.read()))

if __name__ == '__main__':
    for i in range(3):
        print(i)