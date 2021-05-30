from collections import deque

n, m = list(map(int,input().split()))

b = [[0 for i in range(2*n+1)] for j in range(2*n+1)]

for i in range(m):
    x, y  = list(map(int,input().split()))
    b[x][y] = 1

ans = [False for i in range(2*n+1)]
ansi = 0
memo = [[False for i in range(2*n+1)] for j in range(2*n+1)]
que = deque()
que.append([0, n])
while que:
    i, j = que.popleft()
    if memo[i][j]:
        continue
    memo[i][j] = True
    if 0 <= i <= 2*n-1:
        if 0 <= j <= 2*n and b[i+1][j] == 0:
            que.append([i+1, j])
        if 0 <= j <= 2*n-1 and b[i+1][j+1] == 1:
            que.append([i+1, j+1])
        if 0 <= j <= 2*n-1 and b[i+1][j-1] == 1:
            que.append([i+1, j-1])
    else:
        if not ans[j]:
            ans[j] = True
            ansi += 1


print(ansi)
