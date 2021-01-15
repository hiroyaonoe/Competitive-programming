n,l=list(map(int,input().split()))
s=[]
for i in range(l):
    line=input().split("|")
    line.pop()
    s.append(line[1:])

maru=input()

pos=maru.find("o")//2+1

for i in range(l):
    buf=s.pop()
    if pos>1 and buf[pos-2]=="-":
        pos-=1
    else:
        if pos<n and buf[pos-1]=="-":
            pos+=1
print(pos)
