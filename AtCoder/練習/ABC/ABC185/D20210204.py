n,m = list(map(int,input().split()))
a=[]
if m>0:
    a = list(map(int, input().split()))
a.sort()
a.append(n+1)
interval=[]
prev=0

for i in range(m+1):
    tmp=a[i]-prev-1
    if tmp>0:
        interval.append(tmp)
    prev=a[i]

if len(interval)==0:
    print(0)
    exit()

k=min(interval)

ans = 0
for i in interval:
    ans += -(-i // k)

print(ans)


