n=int(input())
s=[]
t=[]

for i in range(n):
    ss,tt=input().split()
    s.append(ss)
    t.append(int(tt))

x=input()

a=s.index(x)

print(sum(t[a+1:]))