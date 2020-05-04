n,k=map(int,input().split())
a=set()
for i in range(k):
    d=input()
    aaa=map(int,input().split())
    for aa in aaa:
        a.add(aa)

print(n-len(a))