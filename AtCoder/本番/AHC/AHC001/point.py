import one
import input

def point(n,xx,yy,rr,ret):
    pp=0
    for i in range(n):
        x=xx[i]
        y=yy[i]
        r=rr[i]
        a,b,c,d = ret[i]

        if a==c or b==d:
            out = "error" + str(i)
            print(out)
            exit()
        s=abs((c-a)*(d-b))
        p=1-(1-min([s,r])/max([s,r]))**2
        print(i,": ",p)
        pp += p
    return int(pp*10**9//n)

def main():
    name = "0000"

    n, x, y, r = input.read_input(name)

    ret = one.one(n, x,y,r)
    for (a,b,c,d) in ret:
        print(a,b,c,d)

    print(point(n,x,y,r,ret))

if __name__=='__main__':
    main()