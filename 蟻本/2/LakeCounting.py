N,M = map(int,input().split(" "))
Gd=[]
for i in range(N):
    Gd.append(list(input()))
def dfs(x,y):
    Gd[x][y]="o"
    for dx in range(-1,2):
        for dy in range(-1,2):
            nx=x+dx
            ny=y+dy
            if (0<=nx<N) & (0<=ny<M):
                if Gd[nx][ny]=="w":dfs(nx,ny)

ans=0
for xx in range(N):
    for yy in range(M):
        if Gd[xx][yy]=="w":
            dfs(xx,yy)
            ans+=1
print(ans)
