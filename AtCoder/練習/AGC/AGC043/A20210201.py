# editorial

h,w= list(map(int,input().split()))
s=[]
for i in range(h):
    s.append(list(input()))

black="#"
white="."
INF=1<<30
dp=[[INF]*w for i in range(h)]
if s[0][0]==black:
    dp[0][0]=1
else:
    dp[0][0]=0
for r in range(h):
    for c in range(w):
        if r>0:
            down=dp[r-1][c]
            if s[r-1][c]==white and s[r][c]==black:
                down+=1
            dp[r][c] = min([dp[r][c], down])
        if c>0:
            right=dp[r][c-1]
            if s[r][c-1]==white and s[r][c]==black:
                right+=1
            dp[r][c] = min([dp[r][c], right])

print(dp[h-1][w-1])


