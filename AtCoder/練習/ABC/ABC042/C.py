n,k=map(int,input().split())
d=input().split()

yet=True
while yet:
    yet=False
    for i in list(str(n)):
        if i in d:
            yet=True
            break
    n+=1

print(n-1)