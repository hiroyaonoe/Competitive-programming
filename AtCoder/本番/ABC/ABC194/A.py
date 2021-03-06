a,b = list(map(int,input().split()))
a += b
if a>=15 and b >= 8:
    p=1
elif a>=10 and b >=3:
    p=2
elif a>=3:
    p=3
else:
    p=4
print(p)