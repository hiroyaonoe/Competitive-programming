# 未完成

def main():
    print("input")
    n = int(input())
    x=[]
    y=[]
    r=[]
    for i in range(n):
        xx, yy, rr = list(map(int, input().split()))
        x.append(xx)
        y.append(yy)
        r.append(rr)
    memo = [[-1 for _ in range(10000)] for _ in range(10000)]
    print("output")
    for i in range(n):
        a, b, c, d = list(map(int, input().split()))
        if not (a <= x[i] < c and b <= y[i] < d):
            print(i,":xy:",x[i],y[i],a,b,c,d)
        invalid = draw(a,b,c,d,i,memo)
        if invalid >= 0:
            print(i, ":",invalid,":", x[i], y[i], a, b, c, d)

def draw(a,b,c,d,num,memo):
    invalid = -1
    for i in range(a,c):
        for j in range(b,d):
            if memo[i][j] >= 0:
                invalid = memo[i][j]
            memo[i][j]=num
    return invalid

if __name__ == '__main__':
    main()
