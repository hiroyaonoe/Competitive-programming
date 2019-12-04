
n,q=map(int,input().split(' '))
c=[]*n
for i in range(n):
    c[i]=chr(65+i)
for i in range(q):
    gomi,c1,c2=map(str,input().split(' '))
    ans=''
    print(ans,flush=True)
    if ans=='>':
        index1=c.index(c1)
        index2=c.index(c2)
        c[index1],c[index2]=c[index2],c[index1]
print('!',''.join(c),flush=True)

