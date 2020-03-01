# n,m=map(int,input().split())
# sc=[]
# ans=0
# no=False
# mm=True
# zero=False
# for i in range(m):
#     ss,cc=map(int,input().split())
#     for q in range(i):
#         if s[q]==ss:
#             if c[q]!=cc:
#                 no=True
#                 break
#             else:
#                 ans-=cc*(10**(n-ss))
#
#     s.append(ss)
#     c.append(cc)
#
#     ans+=cc*(10**(n-ss))
#     if ss==1:
#         mm=False
#         if cc==0:
#             if n>1:no=True
#
# for i in range(m):
#     ss,cc=map(int,input().split())
#     sc.append([ss,cc])
#     for j in range(i-1):
#         if sc[j][0]==ss:
#             if sc[j][1]==cc:
#                 sc.pop()
#
#             else:
#                 no=True
#
# if no:pass
# else:
#     for i in sc:
#         ans+=i[1]*(10**(n-i[0]))
#     if sc[0]==1:
#         mm=False
#         if sc[1]==0:
#
#
#
#
# if mm:
#     ans+=10**n
# if zero:ans=0
# if no:ans=-1
#
#
# print(ans)

n,m=map(int,input().split())
sc=[]
for i in range(m):
    sc.append(list(map(int,input().split())))

mm=10**(n-1)
if n==1:mm-=1
mmm=10**n
for i in range(mm,mmm):
    ok=True
    ii=str(i)
    for j in sc:
        ss=j[0]-1
        cc=j[1]

        if ii[ss]==str(cc):
            pass
        else:
            ok=False
            break
    if ok:
        print(i)
        quit()
print(-1)