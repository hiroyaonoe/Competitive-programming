from itertools import combinations_with_replacement as cmb

n,m,q=map(int,input().split())
abcd=[]
for i in range(q):
    ll=map(int,input().split())
    ll=[ww-1 for ww in ll]
    abcd.append(ll)
ans=0
for li in cmb(range(1,m+1),n):
    kari=0
    for i in abcd:
        if li[i[1]]-li[i[0]]==i[2]+1:
            kari+=i[3]+1
    ans=max(ans,kari)

print(ans)