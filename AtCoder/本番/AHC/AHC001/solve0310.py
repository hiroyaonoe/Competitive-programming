# 重すぎてnが大きいとchanged一周すら出来てない

import time

# x: [x, 入力の順序, ソート後の順序] xでソート
# xs [x, 入力の順序, ソート後の順序] 入力の順序でソート
def one(n, x,y,r):
    start = time.time()
    x.sort(key=lambda i: i[0])
    y.sort(key=lambda i: i[0])
    x.append([10000, n])
    y.append([10000, n])

    for i in range(n + 1):
        x[i].append(i)
        y[i].append(i)
    xs = sorted(x, key=lambda i: i[1])
    ys = sorted(y, key=lambda i: i[1])
    memo = [[-1 for _ in range(10000)] for _ in range(10000)]
    ret = []
    for i in range(n):
        xx = xs[i][0]
        yy = ys[i][0]
        xi = xs[i][2]
        yi = ys[i][2]
        a, b = xx, yy
        if xi == 0:
            a = 0
        if yi == 0:
            b = 0
        jx = xi
        jy = yi
        while x[jx][0] == x[jx + 1][0]:
            jx += 1
        while y[jy][0] == y[jy + 1][0]:
            jy += 1
        c = max(x[jx + 1][0], xx + 1)
        d = max(y[jy + 1][0], yy + 1)
        draw(a, b, c, d, i, memo)
        ret.append([a, b, c, d])

    changed=True
    while changed:
        changed=change(n,ret,x,y,r,memo,start)
        print(time.time() - start)
    return ret

def change(n,ret,xx,yy,rr,memo,start):
    changed=False
    for i in range(n):
        x=xx[i][0]
        y=yy[i][0]
        a,b,c,d=ret[i]
        r=rr[i]
        state=0
        count=-1
        while True:
            if time.time() - start > 4.6:
                return False
            count+=1
            s = (c - a) * (d - b)
            p = point(r, s)
            p_udad = point(r, s+c-a)
            p_udrm = point(r, s-c+a)
            p_lrad = point(r, s+d-b)
            p_lrrm = point(r, s-d+b)
            if state>=0:
                u_ad, d_ad, l_ad, r_ad = False, False, False, False
                run=""
                if p_lrad > p:
                    if can_expand(a - 1, b, a, d, memo):
                        l_ad = True
                    if can_expand(c, b, c + 1, d, memo):
                        r_ad = True
                if p_udad > p:
                    if can_expand(a, b - 1, c, b, memo):
                        u_ad = True
                    if can_expand(a, d, c, d + 1, memo):
                        d_ad = True
                # 0123 =udlr
                if count % 2 == 0:
                    if r_ad:run=3
                    if d_ad:run=1
                    if l_ad:run=2
                    if u_ad:run=0
                else:
                    if d_ad:run=1
                    if r_ad:run=3
                    if u_ad:run=0
                    if l_ad:run=2
                if run==2:
                    draw(a - 1, b, a, d, i, memo)
                    a -= 1
                elif run==3:
                    draw(c, b, c + 1, d, i, memo)
                    c += 1
                elif run==0:
                    draw(a, b - 1, c, b, i, memo)
                    b -= 1
                elif run==1:
                    draw(a, d, c, d + 1, i, memo)
                    d += 1

                if u_ad or d_ad or l_ad or r_ad:
                    state = 1
                    continue
            if state<=0:
                u_rm, d_rm, l_rm, r_rm = False, False, False, False
                run = ""
                if p_lrrm > p:
                    if a + 1 <= x < c:
                        l_rm = True
                    if a <= x < c - 1:
                        r_rm = True
                if p_udrm > p:
                    if b + 1 <= y < d:
                        u_rm = True
                    if b <= y < d - 1:
                        d_rm = True

                if count % 2 == 0:
                    if l_rm: run = 2
                    if u_rm: run = 0
                    if r_rm: run = 3
                    if d_rm: run = 1
                else:
                    if u_rm: run = 0
                    if l_rm: run = 2
                    if d_rm: run = 1
                    if r_rm: run = 3
                if run == "l":
                    draw(a, b, a + 1, d, -1, memo)
                    a += 1
                elif run == "r":
                    draw(c - 1, b, c, d, -1, memo)
                    c -= 1
                elif run == "u":
                    draw(a, b, c, b + 1, -1, memo)
                    b += 1
                elif run == "d":
                    draw(a, d - 1, c, d, -1, memo)
                    d -= 1

                if u_rm or d_rm or l_rm or r_rm:
                    state = -1
                    continue
            break
        ret[i]=[a,b,c,d]
        if count>0:
            changed=True
    return changed

# memoを書き換え
def draw(a,b,c,d,num,memo):
    for i in range(a,c):
        for j in range(b,d):
            memo[i][j]=num

# その範囲内が１マスでも埋まっていたらFalse
def can_expand(a,b,c,d,memo):
    if a<0 or b<0 or c<0 or d<0:return False
    if a>10000 or b>10000 or c>10000 or d>10000:return False
    for i in range(a,c):
        for j in range(b,d):
            if memo[i][j]>=0:
                return False
    return True

def point(r,s):
    return 1-(1-min([s,r])/max([s,r]))**2

def main():
    n = int(input())
    x=[]
    y=[]
    r=[]
    for i in range(n):
        xx, yy, rr = list(map(int, input().split()))
        x.append([xx,i])
        y.append([yy,i])
        r.append(rr)
    ret = one(n, x,y,r)
    for (a,b,c,d) in ret:
        print(a,b,c,d)


if __name__ == '__main__':
    main()
