# editional
n=int(input())

ab=[]
ans=0
for i in range(n):
    aa,bb=list(map(int,input().split()))
    ans-=bb
    ab.append(aa+bb)

ab.sort()

for i in range(n):
    q=ab.pop()
    if i%2==0:
        ans+=q

print(ans)

# # 多次元配列のソート
# from operator import itemgetter
#
# n=int(input())
#
# ab=[]
# for i in range(n):
#     aa,bb=list(map(int,input().split()))
#     ab.append([aa,bb,i])
#
# a=sorted(ab,key=itemgetter(0,1))
# b=sorted(ab,key=itemgetter(1,0))
# idx=[False for i in range(n)]
# isA=True
# l=a
# ans=0
# while (len(l)>0):
#     if isA:
#         l=a
#     else:
#         l=b
#     x, y, id = l.pop()
#
#     if idx[id]:continue
#
#     if isA:
#         ans+=x
#     else:
#         ans-=y
#
#     idx[id]=True
#     isA= not isA
#
# print(ans)

