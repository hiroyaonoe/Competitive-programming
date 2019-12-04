N,A,B=map(int,input().split(" "))
cnt = 0
for j in range(1,N+1):
    i = j
    num = 0
    while(True):
        res = i%10
        i = (i-res)/10
        num += res
        if i == 0:break
    if A<=num<=B:cnt+=j
print(cnt)