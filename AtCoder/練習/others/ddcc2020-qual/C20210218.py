# editorial

h, w, k = list(map(int, input().split()))
s = []
cut_h = [False for i in range(h)]
first = True
for i in range(h):
    ss = list(input())
    if '#' in ss:
        if first:
            first = False
        else:
            cut_h[i] = True
    s.append(ss)
cut_h[0] = True

cnt = 0
idx = 0
berry = [False for i in range(w)]
for i in range(h):
    if cut_h[i]:
        first = True
        out_l = []
        for j in range(w):
            if berry[j]:
                if not first:
                    cnt += 1
            first = False
            out_l.append(str(cnt))
        out = " ".join(out_l)
        for p in range(i - idx):
            print(out)

        idx = i
        cnt += 1
        berry = [False for i in range(w)]
    for j in range(w):
        if s[i][j] == '#':
            berry[j] = True

first = True
out_l = []
for j in range(w):
    if berry[j]:
        if not first:
            cnt += 1
    first = False
    out_l.append(str(cnt))
out = " ".join(out_l)
for p in range(h - idx):
    print(out)
