import os
from selenium import webdriver
def writes(str):
    with open("baidus.txt","w+",encoding="UTF-8") as r:
        r.write("\n"+str)
def reads():
    with open("baidus.txt", "r",encoding= "utf-8") as r:
        lines = r.read()
        return lines
def write(str):
    with open("baidu.txt","a",encoding="UTF-8") as r:
        r.write("\n"+str)
def read():
    with open("baidu.txt", "r",encoding= "utf-8") as r:
        lines = r.readlines()
        return lines[-2]
def driver(url=None):
    driver = webdriver.Chrome(os.getcwd() + "\\File\\chromedriver.exe")
    if url is None:
        pass
    else:
        driver.get(url)
    return driver

i = 753732
print(reads())
url = read()
driver = driver(url)
try:
    x = driver.find_element_by_xpath("//*[@id=\"content\"]").text
    y = driver.find_element_by_xpath("//*[@id=\"wrapper\"]/div[5]/div/div[4]/a[4]").get_attribute("href")
    z = driver.find_element_by_xpath("//*[@id=\"wrapper\"]/div[5]/div/div[2]/h1").text
    writes(x)
    write(y)
    write(z)
    driver.quit()
except Exception as e:
    print(e)
    driver.quit()