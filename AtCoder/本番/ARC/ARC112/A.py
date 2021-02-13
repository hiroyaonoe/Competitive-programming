t = int(input())

for i in range(t):
    l,r = list(map(int,input().split()))
    p = max(r-2*l+1,0)
    ans = p*(p+1)//2
    print(ans)