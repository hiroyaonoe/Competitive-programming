import bisect
n=int(input())
L=[]*n
L=list(map(int,input().split()))
L.sort()
cnt=0
for i in range(n-2):
    for j in range(i+1,n-1):
        ab=L[i]+L[j]
        num=bisect.bisect_left(L,ab,j+1,n)-j-1 # bisect_left(L[j+1:],ab)は遅い
        cnt+=num
print(cnt)