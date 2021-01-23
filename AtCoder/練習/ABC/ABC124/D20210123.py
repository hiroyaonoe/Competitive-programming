# editional
n,k = list(map(int,input().split()))
s=input()
s=[i=="1" for i in s]
k=int(k)

block = []

add=0
now=1
for i in s:
    if i==now:
        add+=1
    else:
        block.append(add)
        add = 1
        now = i
block.append(add)

if not len(block) % 2:
    block.append(0)

if len(block) <= 2*k+1:
    print(n)
    exit()

current = sum(block[:2*k+1])
ans=current

for i in range(0,len(block)-2*k-1,2):
    current += block[2*k+1+i] + block[2*k+i+2] - block[i] - block[i+1]
    ans = max(ans, current)
print(ans)