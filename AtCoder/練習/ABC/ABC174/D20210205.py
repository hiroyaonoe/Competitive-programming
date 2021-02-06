# editorial

n=int(input())
c=list(input())

w=0
r=c.count("R")

ans=max(w,r)
for i in c:
    if i=="R":
        r -= 1
    else:
        w += 1
    ans = min(ans,max(w,r))

print(ans)