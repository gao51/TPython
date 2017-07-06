

ln_path = 'G:/code/test/test2.txt'
fn_path = 'G:/code/test/test1.txt'
fn = []
ln1 = []
ln2 = []
with open(fn_path,'r',encoding='ANSI') as f:
    #print ('-------',f.readlines())
    for line in f.readlines():
        fn.append(line.split('\n')[0])
f.close()
fn = tuple(fn)
with open(ln_path,'r',encoding="ansi")as f:
    for line in f.readlines():
        if len(line.split('\n')[0])==1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])
f.close()
ln1 = tuple(ln1)
ln2 = tuple(ln2)

import random
class FakeUser:
    def fake_name(self,amount = 1,one_word=False,two_words = False):
        n= 0
        while n<=amount:
            if one_word:
                full_name = random.choice(fn)+random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn)+random.choice(ln2)
            else:
                full_name = random.choice(fn)+random.choice(ln1+ln2)
            yield full_name
            n+=1
#        print(full_name)
    def fake_gender(self,amount=1):
        n=0
        while n <= amount:

            gender = random.choice(['男','女','未知'])
            yield gender
            n += 1
class SnsUser(FakeUser):
    def get_follower(self,amount =1,few = True,a_lot = False):
        n = 0
        while n <= amount:

            if few:
                followers = random.randrange(1,50)
            elif a_lot:
                followers =random.randrange(200,10000)
            yield followers
            n +=1
#        print(followers)

user_a = FakeUser()
user_b  = SnsUser()
for name in user_a.fake_name(30):
    print(name)
for gender in user_a.fake_gender(30):
    print(gender)
