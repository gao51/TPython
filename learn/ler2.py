# -*-coding:UTF-8-*-
# _author_= 'gao'
ln_path = 'G:/code/test/test1.txt'
fn = []
with open(ln_path,'r') as f:
    str = f.readlines()
    print str
    print len(str)


