# 動的計画法
import sys
input=sys.stdin.readline

n=int(input())
s=input()
dp=[[[False]*1000 for j in range(4)] for i in range(n+1)]

dp[0][0][0]=True

for i in range(n):
    for j in range(4):
        for k in range(1000):
            if dp[i][j][k]==False:continue
            dp[i+1][j][k]=True
            if j<=2:
                dp[i+1][j+1][k*10+int(s[i])]=True
cnt=0
for i in range(1000):
    if dp[n][3][i]==1:cnt+=1
print(cnt)