s=input()

odd=True
a=ord("a")
z=ord("z")
for i in s:
    if odd:
        if not (a <= ord(i) <= z):
            print("No")
            exit()
    else:
        if a <= ord(i) <= z:
            print("No")
            exit()
    odd = not odd
print("Yes")