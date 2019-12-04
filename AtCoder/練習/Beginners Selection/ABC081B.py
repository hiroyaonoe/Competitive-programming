n=int(input())
a=list(map(int,input().split(" ")))
cnt=-1
loop=True
while loop:
    for i in range(n):
        if a[i]%2==0:
            a[i]/=2
        else:
            loop=False
            break
    cnt+=1
print(cnt)