n=int(input())
ng=[0,0,0]
ng[0]=int(input())
ng[1]=int(input())
ng[2]=int(input())

m=[0 for i in range(301)]

for i in ng:
    m[i]=-1

for i in range(n+1):
    if m[i]==-1:continue
    buf=[]
    for j in range(3):
        if i>j and m[i-j-1]!=-1:
            buf.append(m[i-j-1]+1)
    if len(buf)>0:
        memo = min(buf)
    else:
        if i==0:
            memo = 0
        else:
            memo = -1
    if memo>100:
        memo = -1
    m[i]=memo

if m[n]==-1:
    print("NO")
else:
    print("YES")
