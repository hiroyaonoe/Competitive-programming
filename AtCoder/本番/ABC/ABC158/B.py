n,a,b=map(int,input().split())
ans=0
# end=True
# while end:
#     if n>=a:
#         n-=a
#         ans+=a
#         if n>b:n-=b
#         else:end=False
#     else:
#         ans+=n
#         end=False

cnt=n//(a+b)
ans+=cnt*a
ama=n%(a+b)
if ama-a>=0:ans+=a
else:ans+=ama
print(ans)