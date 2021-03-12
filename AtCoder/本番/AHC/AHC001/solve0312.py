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

    for i in range(3):
        changed = change(n,ret,x,y,r,memo,start)
        if not changed:break
    return ret

def change(n,ret,xx,yy,rr,memo,start):
    changed=False
    for i in range(n):
        rate = 1 << 6
        x=xx[i][0]
        y=yy[i][0]
        a,b,c,d=ret[i]
        r=rr[i]
        s = (c - a) * (d - b)
        count=0
        if s < r:
            yet=True
            while yet:
                if time.time() - start > 4.7:
                    ret[i] = [a, b, c, d]
                    return False
                a, b, c, d, yet = s_add(i, a, b, c, d, x, y, r, memo, count, rate)
                if not yet: rate = rate // 2
                count+=1

        if s > r:
            yet=True
            while yet and rate > 0:
                if time.time() - start > 4.8:
                    ret[i] = [a, b, c, d]
                    return False
                a, b, c, d, yet = s_rmv(i, a, b, c, d, x, y, r, memo, count, rate)
                if not yet: rate = rate // 2
                count+=1

        ret[i] = [a, b, c, d]
        if count>0:
            changed=True
    return changed

def s_add(i,a,b,c,d,x,y,r,memo,count, rate):
    s = (c - a) * (d - b)
    p = point(r, s)
    p_udad = point(r, s + (c - a)*rate) > p
    p_lrad = point(r, s + (d - b)*rate) > p
    run = -1
    # 0123 =udlr
    if count % 2 == 0: # uldr
        if   p_udad and can_expand(a, b - rate, c, b, memo): run = 0
        elif p_lrad and can_expand(a - rate, b, a, d, memo): run = 2
        elif p_udad and can_expand(a, d, c, d + rate, memo): run = 1
        elif p_lrad and can_expand(c, b, c + rate, d, memo): run = 3
    else: # lurd
        if   p_lrad and can_expand(a - rate, b, a, d, memo): run = 2
        elif p_udad and can_expand(a, b - rate, c, b, memo): run = 0
        elif p_lrad and can_expand(c, b, c + rate, d, memo): run = 3
        elif p_udad and can_expand(a, d, c, d + rate, memo): run = 1

    if run == 0:
        draw(a, b - rate, c, b, i, memo)
        b -= rate
    elif run == 1:
        draw(a, d, c, d + rate, i, memo)
        d += rate
    elif run == 2:
        draw(a - rate, b, a, d, i, memo)
        a -= rate
    elif run == 3:
        draw(c, b, c + rate, d, i, memo)
        c += rate

    return a, b, c, d, run >= 0

def s_rmv(i,a,b,c,d,x,y,r,memo,count,rate):
    s = (c - a) * (d - b)
    p = point(r, s)
    p_udrm = point(r, s + (a - c)*rate) > p
    p_lrrm = point(r, s + (b - d)*rate) > p
    run = -1
    # 0123 =udlr
    if count % 2 == 0: # drul
        if   p_udrm and b <= y < d - rate: run = 1
        elif p_lrrm and a <= x < c - rate: run = 3
        elif p_udrm and b + rate <= y < d: run = 0
        elif p_lrrm and a + rate <= x < c: run = 2
    else: # rdlu
        if   p_lrrm and a <= x < c - rate: run = 3
        elif p_udrm and b <= y < d - rate: run = 1
        elif p_lrrm and a + rate <= x < c: run = 2
        elif p_udrm and b + rate <= y < d: run = 0

    if run == 0:
        draw(a, b, c, b + rate, -1, memo)
        b += rate
    elif run == 1:
        draw(a, d - rate, c, d, -1, memo)
        d -= rate
    elif run == 2:
        draw(a, b, a + rate, d, -1, memo)
        a += rate
    elif run == 3:
        draw(c - rate, b, c, d, -1, memo)
        c -= rate

    return a, b, c, d, run >= 0

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
