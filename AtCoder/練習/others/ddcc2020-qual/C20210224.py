h,w,k = list(map(int,input().split()))
s=[]

def row(r):
    return "#" in s[r]

def col(c,start,end):
    for i in range(start,end):
        if s[i][c]=="#":
            return True
    return False

for i in range(h):
    ss=list(input())
    s.append(ss)

h_cut = []
for i in range(h):
    if row(i):
        h_cut.append(i)
h_cut[0]=0
hl=len(h_cut)
h_cut.append(h)

cnt=1
for i in range(hl):
    w_cut=[]
    for j in range(w):
        if col(j,h_cut[i],h_cut[i+1]):
            w_cut.append(j)
    w_cut[0]=0
    wl=len(w_cut)
    w_cut.append(w)
    out_l=[]
    for k in range(wl):
        add=[str(cnt)]*(w_cut[k+1]-w_cut[k])
        out_l.append(" ".join(add))
        cnt+=1
    out=" ".join(out_l)

    for k in range(h_cut[i+1]-h_cut[i]):
        print(out)
