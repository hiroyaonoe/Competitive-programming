s=input()
k=int(input())
l=len(s)
sub=set()
for i in range(k):
    for j in range(l-i):
        sub.add(s[j:j+i+1])
sub=list(sub)
sub.sort()

print(sub[k-1])