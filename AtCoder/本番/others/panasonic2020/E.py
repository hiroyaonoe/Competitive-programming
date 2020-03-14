

abc=[]
for i in range(3):
    abc.append(input())
    ansabc=abc.copy()

kasa=[[0,0] for i in range(3)]
for i in range(3):
    left=abc[i]
    for j in range(2):
        right=abc[(i+j+1)%3]

        q=min(len(left),len(right))
        for k in range(q):
            # ok=True
            # for e in range(k):
            #     if left[-k+e-1]==right[e]:
            #         if left[-k+e-1]=="?":
            #             ansabc[i]=ansabc[i][:-k + e - 1]+"a"+ansabc[i][-k + e :]
            #             ansabc[(i+j+1)%3]=ansabc[(i+j+1)%3][:-k + e - 1]+"a"+ansabc[(i+j+1)%3][-k + e :]
            #
            #     elif left[-k+e-1]=="?":
            #         ansabc[i] = ansabc[i][:-k + e - 1] + right[e] + ansabc[i][-k + e:]
            #
            #     elif right[e]=="?":
            #         ansabc[(i+j+1)%3]=ansabc[(i+j+1)%3][:-k + e - 1]+left[-k+e-1]+ansabc[(i+j+1)%3][-k + e :]
            #     else:
            #         ok=False

            if left[-k-1]==right[k]:
                kasa[i][j]+=1
            elif left[-k-1]=="?":
                kasa[i][j] += 1
                left[-k - 1]=right[k]
            elif right[k]=="?":

            else:break


vec=[]
for i in range(3):
    for j in range(2):
        vec.append([kasa[i][j],i,j])

vec.sort(reverse=True,key=lambda x: x[0])

fir=vec[0]
sec=vec[1]

if (fir[1]==sec[2])&(fir[2]==sec[1]):
    sec=vec[2]

lfir=fir[1]%3
rfir=(fir[1]+fir[2]+1)%3

lsec=sec[1]%3
rsec=(sec[1]+sec[2]+1)%3

if lfir==rsec:
    jun=[lsec,rsec,rfir]
    lkasa=sec[0]
    rkasa=fir[0]
else:
    jun=[lfir,rfir,rsec]
    lkasa=fir[0]
    rkasa=sec[0]

kkaa=[lkasa,rkasa]

for i in range(2):
    left=abc[jun[i]]
    right=abc[jun[i+1]]
    for k in range(kkaa[i]):

## ここから?を置換する処理をしたい
## しかし？がダブったときの処理ができない

ans=ansabc[jun[0]][0:-lkasa]+ansabc[jun[1]][0:-rkasa]+ansabc[jun[2]]
print(ans)






