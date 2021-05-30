n, k = list(map(int, input().split()))

a = []
lim = (k * k) // 2 + 1
ok = 0

for i in range(n):
    ai = list(map(int, input().split()))
    a.append(ai)
    mxi = max(ai)
    if ok < mxi:
        ok = mxi

ng = -1

while ng+1 < ok:
    x = (ng + ok) // 2
    s = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i-1][j-1] > x:
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + 1
            else:
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
    ext = False
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            if s[i + k][j + k] + s[i][j] - s[i][j + k] - s[i + k][j] < lim:
                ext = True
    if ext:
        ok = x
    else:
        ng = x

print(ok)