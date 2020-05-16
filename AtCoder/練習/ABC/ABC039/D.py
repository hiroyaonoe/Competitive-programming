h,w=list(map(int,input().split()))

s=[]
ok=[]
ans=[]
for i in range(h):
    sss=list(input())
    s.append(sss)
    ok.append(sss.copy())

    ans.append(['.' for j in range(w)])

for y in range(h):
    for x in range(w):
        around=[[0,0,0],
                [0,0,0],
                [0,0,0]]

        for dy in (-1,0,1):
            if not(0<=y+dy<h):
                around[1+dy]=[1,1,1]
                continue
            for dx in (-1,0,1):
                if not(0<=x+dx<w):
                    around[1+dy][1+dx]=1
                    continue
                if s[y+dy][x+dx]=="#":
                    around[1+dy][1+dx]=1

        if sum(map(sum,around))==9:
            ans[y][x]="#"
            for dy in (-1, 0, 1):
                if not (0 <= y + dy < h):
                    continue
                for dx in (-1, 0, 1):
                    if not (0 <= x + dx < w):
                        continue
                    ok[y+dy][x+dx]="."


for y in range(h):
    for x in range(w):
        if ok[y][x]!='.':
            print("impossible")
            exit()

print("possible")
for y in range(h):
    row="".join(ans[y])
    print(row)