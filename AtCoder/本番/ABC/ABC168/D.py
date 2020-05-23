import sys
sys.setrecursionlimit(2000000)

n,m=list(map(int,input().split()))

lis=[set() for i in range(n)]

for i in range(m):
    aa,bb=list(map(int,input().split()))
    lis[aa-1].add(bb-1)
    lis[bb-1].add(aa-1)


mic=[None for i in range(n)]
pas=[None for i in range(n)]
pas[0]=0
def search(mae,x,length):
    length+=1
    for i in lis[x]:
        if i in mae:
            continue


        if pas[i]==None:
            mic[i]=x
            pas[i]=length
        else:
            if length<pas[i]:
                mic[i]=x
                pas[i]=length

        search(mae+[i],i,length)



search([],0,0)
mic.pop(0)

if None in mic:
    print('No')
else:
    print('Yes')
    for i in range(n-1):
        print(mic[i]+1)


