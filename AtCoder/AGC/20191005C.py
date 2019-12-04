N = int(input())
X = int(input())
ans  = 0
for i in range(X+1):
    cnt = 0
    ttt = True
    P = i
    while(ttt):
        if P % 2 ==1:
            P = (P-1)/2
        else:
            P = P/2+2^(N-1)
        if P != i:
            cnt += 1
        else:
            ttt == False
            ans += cnt
