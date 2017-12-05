# -*-coding:UTF-8-*-
# _author_= 'gao'

print([(x,y) for x in range(4) for y in range(4)])

print (sum(range(10)))

print (range(10))

for letter in 'Runoob':
    if letter == 'o':
        pass
        print ("执行 pass 块")
    print ("当前字母 :"+ letter)
print ("Good bye!")