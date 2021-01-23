n,x= list(map(int,input().split()))
x *= 100
s=0
for i in range(n):
    v,p= list(map(int,input().split()))
    s+=v*p
    if s>x:
        print(i+1)
        exit()
print(-1)