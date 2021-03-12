
def read_input(name):
    with open("ded8fd3366b4ff0b0d7d053f553cdb84/tools/in/"+name+".txt", "r") as f:
        line = f.readline()
        n=int(line.rstrip("\n"))
        x = []
        y = []
        r = []
        for i in range(n):
            line = f.readline()
            xx,yy,rr = list(map(int,line.rstrip("\n").split()))
            x.append([xx, i])
            y.append([yy, i])
            r.append(rr)

    return n,x,y,r
