# -*-coding:UTF-8-*-
# _author_= gao

import json

js = '{"confPriority": 0, "formList": [{"formId": 2}, {"formId": 3}], "maxMultiFormImgCount": -1}'
j=json.loads(js)

print(j)
print(type(j))

print(j["formList"][0])