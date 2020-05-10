

z=ord('z')
a=ord('a')
ss=input()
s=list(ss)
k=int(input())
l=len(s)

for i in range(l):
    if (z-ord(s[i])+1<=k)and(s[i]!='a'):
        k-=z-ord(s[i])+1
        s[i]='a'

if k>0:
    last=(ord(s[-1])+k-a)%26+a
    s[-1]=chr(last)

ans=''.join(s)
print(ans)