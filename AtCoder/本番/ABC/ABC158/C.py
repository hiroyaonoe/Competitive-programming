from math import floor
a,b=map(int,input().split())

root=floor(a*100//8)

while True:
    if (a==int(floor(root*0.08)))&(b==int(floor(root*0.1))):
        ans=int(root)
        break
    else:
        if (int(floor(root*0.08))>a)|(int(floor(root*0.1))>b):
            ans=-1
            break
        root+=1
print(ans)
