n=int(input())
a=list(map(int,input().split()))
ans=set()
while len(a)>0:
    k=a.pop()
    while True:
        if k%2==0:
            k=k//2
        else:
            break
    ans.add(k)

print(len(ans))