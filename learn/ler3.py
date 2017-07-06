class aaa():
    def a(self,m,n):
        return [(x,y) for x in range(m) for y in range(n)]
mn = aaa();
print(mn.a(5,2))