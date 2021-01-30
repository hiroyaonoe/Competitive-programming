n,s,d= list(map(int,input().split()))

for i in range(n):
    x,y= list(map(int,input().split()))
    if x<s and y>d:
        print("Yes")
        exit()
print("No")