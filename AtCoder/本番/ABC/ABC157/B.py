a=[]
for i in range(3):
    a.append(list(map(int,input().split())))
n=int(input())
aa=[[False for i in range(3)] for j in range(3)]
for i in range(n):
    b=int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k]==b:
                aa[j][k]=True

bingo=False

for i in range(3):
    if aa[i][0] & aa[i][1] & aa[i][2]:
        bingo=True

for i in range(3):
    if aa[0][i] & aa[1][i] & aa[2][i]:
        bingo=True

if aa[0][0] & aa[1][1] & aa[2][2]:
    bingo=True

if aa[0][2] & aa[1][1] & aa[2][0]:
    bingo=True

if bingo:print("Yes")
else:print("No")