x,n=list(map(int,input().split()))
p=list(map(int,input().split()))

i = 0
while True:
    if x-i not in p:
        print(x-i)
        exit()
    if x+i not in p:
        print(x+i)
        exit()
    i+=1
