n=int(input())

takagi=0
gain=[]
for i in range(n):
    a,b= list(map(int,input().split()))
    takagi-=a
    gain.append(a*2+b)

gain.sort(reverse=True)

for i in range(n):
    takagi += gain[i]
    if takagi > 0:
        print(i+1)
        exit()
