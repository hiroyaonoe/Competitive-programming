n=int(input())

e=True
for i in range(n):
    a=int(input())
    if a%2==1:
        e=False

if e:
    print("second")
else:
    print("first")

