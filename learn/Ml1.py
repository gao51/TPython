# -*-coding:UTF-8-*-
# _author_= 'gao'

import hashlib

def md5(str):
    import hashlib
    import types
    if type(str) is types.IntType:
        print ("-------"+type(str))
        str = str(str)
        print ("+++++++" + type(str))
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

a = 123456
b = str(a)
print (md5(a))