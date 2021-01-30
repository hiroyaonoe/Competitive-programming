n=int(input())

a= list(map(int,input().split()))
s=0
p=[0 for i in range(n)]
idx=[1 for i in range(n)]
for i,aa in enumerate(a):
    q=sum(idx[:aa])
    p[i]=q
    s+=q
    idx[aa]=0



#
# print(s)
# for i in range(n-1):
#     s = s + n - p[i]*2 -1
#     print(s)
