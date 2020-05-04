k=int(input())
a,b=map(int,input().split())

aa=a-a%k
ans=False
while aa<=b:
    if a<=aa<=b:
        ans=True
        break
    aa+=k
if ans:print("OK")
else:print("NG")
