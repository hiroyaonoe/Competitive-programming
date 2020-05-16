k=int(input())

dp=[[] for i in range(10**4)]

if k<=9:
    print(k)
    exit()

dp[1]=[str(i) for i in range(1,10)]

n=9
i=1
while n<k:
    for mo in dp[i]:
        simo=int(mo[-1])
        rr=[str(simo-1),str(simo),str(simo+1)]
        for r in rr:
            if 0<=int(r)<=9:
                n+=1
                gen=mo+r
                dp[i+1].append(gen)
                if n==k:
                    ans=gen
                    print(ans)
                    exit()
    i+=1