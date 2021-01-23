n=int(input())
s=[]
for i in range(n):
    ss=input()
    if ss=="AND":
        s.append(True)
    else:
        s.append(False)

ans=1
for i in reversed(range(n)):
    if not s[i]:
        ans+=1 << (i+1)

print(ans)