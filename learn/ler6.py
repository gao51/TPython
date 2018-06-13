# -*-coding:UTF-8-*-
# _author_= 'gao'
import xlrd


def aaa(path, name, col):
    re = []
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(name)
    for i in range(col):
        x = table.col_values(i)
        re.append(x)
    return re


# s = aaa("C:\\Users\\gao\\Desktop\\ddd.xlsx","Sheet1",7)
# print(s)
c = [2.0, 4.0, 6.0]

from pylab import *

x = [2.0, 4.0, 6.0,4,2,1,9,5,7,2]
y = []
l=[2,6,3]
m = [-1,-2,-3]
count = 0
for i in x:
    count -=1
    y.append(count)
plt.figure(figsize=(8, 4))
plt.plot(x, y, "b--", linewidth=1)
plt.plot(l, m, "r--", linewidth=1)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Line plot")
plt.show()
