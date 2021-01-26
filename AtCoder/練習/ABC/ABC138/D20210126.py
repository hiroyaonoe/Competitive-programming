n,q= list(map(int,input().split()))
e=[[] for i in range(n)]
for i in range(n-1):
    a,b= list(map(int,input().split()))
    a-=1
    b-=1
    e[a].append(b)
    e[b].append(a)

imos=[0 for i in range(n)]
for i in range(q):
    p,x= list(map(int,input().split()))
    p-=1
    imos[p]+=x

que = []
que.append([0,-1])
while len(que)>0:
    i,prev=que.pop()
    add=imos[i]
    for v in e[i]:
        if v==prev:continue
        imos[v] += add
        que.append([v,i])

print(" ".join(map(str,imos)))

# PyPyは+による長い文字列の結合が遅い
# joinならPyPyは高速
# https://qiita.com/OKCH3COOH/items/f0c5c4681bc30dddf7f4
# ans=""
# for i in imos:
#     ans += str(i) + " "
#
# print(ans[:-1])