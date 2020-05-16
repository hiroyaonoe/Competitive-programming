x=input()

l=len(x)
stock=0

for i in list(x):
    if i=='S':
        stock+=1
    else:
        if stock>0:
            stock-=1
            l-=2

print(l)