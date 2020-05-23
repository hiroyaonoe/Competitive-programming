a,b,k=list(map(int,input().split()))

cnt=0
for i in reversed(range(1,min(a,b)+1)):
    if (a%i==0) & (b%i==0):
        cnt+=1
    if cnt==k:
        print(i)
        exit()