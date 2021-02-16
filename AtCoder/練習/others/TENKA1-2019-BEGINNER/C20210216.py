n=int(input())
s=input()
black=[0]
white=0

for i in range(n):
    num = black[-1]
    if s[i]=='#':
        num += 1
    else:
        white += 1
    black.append(num)

ans=[]

for i,b in enumerate(black):
    w = white + b - i - 1
    ans.append(b+w)
print(min(ans)+1)