from datetime import date
from profile import run

import requests
import re

import time


# url = "http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sh600802&scale=5&ma=no&datalen=1"
# url = "http://hq.sinajs.cn/list=sh600802"
# while True:
#     request = requests.get(url)
#     result = request.text.split(",")
#     response = request.text[1:-1]
#     res = re.findall(r"low(.+?)close", response)
#     print(time.strftime("%a %b %d %H:%M:%S", time.localtime()),">>>>>>>>now:",end='')
#     print(result[3],">>>max:",result[4],">>>min:",result[5])
#     time.sleep(5)
# # url1 = "https://ams-test1.fishsaying.com/a/login?new=1"
# url = "https://ams-test1.fishsaying.com/a/v2/cms/article/list?pageSize=20&pageNo=1&delFlag=0&auditStatus=0"
# data = {"username":"admin","password":"admin"}
# requ=requests.post(url1,data=data)
# cookies = requ.cookies
# print(requ.cookies)
# request = requests.get(url,cookies=cookies)
# print(request.text)
from flask import json


def wait():
    # todo wait to creat user and password
    pass


def code(name):
    url = "http://hq.sinajs.cn/list=" + name
    # sh600802
    while True:
        # request = requests.get(url)
        try:
            request = requests.get(url)
            # requests = requests.get("http://hq.sinajs.cn/list=sh000001")
        except Exception as e:
            print("fanhui")
            print(request.text)
            print(e)

        finally:
            result = request.text.split(",")
            # results = requests.text.split(",")
            # print(time.strftime("%a %b %d %H:%M:%S", time.localtime()), ">>>>>>>>now:", end='')
            # print(results[3], ">>>max:", results[4], ">>>min:", results[5])

            print(time.strftime("%a %b %d %H:%M:%S", time.localtime()), ">>>>>>>>now:", end='')
            print(result[3], ">>>max:", result[4], ">>>min:", result[5])
        time.sleep(5)


def coder(name):
    url = "http://hq.sinajs.cn/list=" + name
    try:
        request = requests.get(url)
        # requests = requests.get("http://hq.sinajs.cn/list=sh000001")
    except Exception as e:
        print("fanhui")
        print(request.text)
        print(e)

    finally:

        try:
            result = request.text.split(",")
        except Exception as e:
            print(e)
        finally:
            pass
        #print(result)
        # results = requests.text.split(",")
        # print(time.strftime("%a %b %d %H:%M:%S", time.localtime()), ">>>>>>>>now:", end='')
        # print(results[3], ">>>max:", results[4], ">>>min:", results[5])
        # print(name+"**"+name1,end='')
        # print(time.strftime("%a %b %d %H:%M:%S", time.localtime()), ">>>>>>>>now:", end='')
        # print(result[3], ">>>max:", result[4], ">>>min:", result[5])
        # print("**********")
        zd = 100 * (float(result[3]) - float(result[2])) / float(result[1])
        zd = '%.2f' % zd
        name = result[0].replace('var hq_str_','').replace('"','')
        a= {}
        a["name"] = name
        a["now"] = result[3]
        a["first"] = result[1]
        a["Change"] = zd
        a["max"] = result[4]
        a["min"] = result[5]
        #print(a)
        print(name, '>>>now:', result[3], '>>>kai:',result[1],'>>>zd:', zd, "%,>>>max:", result[4], ">>>min:", result[5])
    return json.dumps(a,ensure_ascii=False)

def start():
    try:
        while True:
            coder("sh000001")
            coder("sz300715")
            coder("sz000572")
            coder("sz300209")
            coder("sh600699")
            coder("sh600797")
            coder("sz000973")
            coder("sh601002")
            coder("sz000906")
            coder("sz000018")
            time.sleep(5)
    except Exception as e:
        print('****************************************************************************')
        time.sleep(10)
        start()

if __name__ == '__main__':
    start()