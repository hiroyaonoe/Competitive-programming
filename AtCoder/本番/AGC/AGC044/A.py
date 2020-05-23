t=int(input())
abc=[2,3,5]

def ans(n,a,b,c,d):
    coin=[a,b,c]
    rets=[]
    for nn in range(n-4,n+5):
        ret = d*abs(n-nn)
        ok = [0 for i in range(3)]
        for i in range(3):
            div=abc[i]
            nabc=nn
            while True:
                if nabc%div==0:
                    ok[i]+=1
                    nabc/=div
                else:
                    break

        so=int(nn/((2**ok[0])*(3**ok[1])*(5**ok[2])))
        ret+=so*d

        for i in range(3):
            div = abc[i]
            for j in range(ok[i]):
                so*=div
                ret+=min((div-1)*so*d,coin[i])
        rets.append(ret)
        print(ret,nn)
    print(min(rets))


for i in range(t):
    n, a, b, c, d = list(map(int, input().split()))
    ans(n,a,b,c,d)