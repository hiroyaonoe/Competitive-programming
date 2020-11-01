n=int(input())
a=list(map(int,input().split()))

if n==2:
    print(a[0]-a[1])
    exit()
su=sum(a)
s=[0 for i in range(n)]
s[0]=a[0]*2-su
for i in range(1,n):
    s[i]=s[i-1]+a[i]*2

s=[abs(i) for i in s][1:-1]

print(min(s))

