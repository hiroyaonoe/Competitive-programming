# 解説AC

x,y,a,b,c=list(map(int,input().split()))
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
p=p[:x]
q=q[:y]
r.extend(p)
r.extend(q)
r.sort(reverse=True)

ans=sum(r[:x+y])

print(ans)

