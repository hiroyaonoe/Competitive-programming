# editorial

h,w,k = list(map(int,input().split()))
s=[]
compressed=[]
h_num=[]
idx=-1
berry=[False for i in range(w)]
for i in range(h):
    ss = list(input())
    ok=False
    for j in range(w):
        if ss[j]=='#':
            berry[j]=True
            ok=True
    if ok:
        compressed.append(berry)
        berry = [False for i in range(w)]
        h_num.append(i-idx)
        idx=i

        for j in range(w):


for berry
cnt=0
idx=0
berry=[False for i in range(w)]
for i in range(h):
    if cut_h[i]:
        first=True
        out_l=[]
        for j in range(w):
            if berry[j]:
                if not first:
                    cnt += 1
            first=False
            out_l.append(str(cnt))
        out=" ".join(out_l)
        for p in range(i-idx):
            print(out)

        idx=i
        cnt += 1
        berry=[False for i in range(w)]
    for j in range(w):
        if s[i][j]=='#':
            berry[j]=True

first=True
out_l=[]
for j in range(w):
    if berry[j]:
        if not first:
            cnt += 1
    first=False
    out_l.append(str(cnt))
out=" ".join(out_l)
for p in range(h-idx):
    print(out)
