
s = input()
t = int(input()) - 1

x=0
y=0
q=0
for c in s:

    if c == "L":
        x-=1
    elif c == "R":
        x+=1
    elif c == "U":
        y+=1
    elif c == "D":
        y-=1
    else:
        q+=1

for i in range(q):
    if x > 0:
        if t:x-=1
        else:x+=1
    elif x < 0:
        if t:x+=1
        else:x-=1
    else:
        if y > 0:
            if t:y -= 1
            else:y += 1
        elif y < 0:
            if t:y += 1
            else:y -= 1
        else:
            x+=1


print(abs(x) + abs(y))

# def move(x,y,s):
#     if s=="":
#         pos.add(abs(x)+abs(y))
#         return
#     c=s[0]
#     ne=s[1:]
#     if c=="L":
#         move(x - 1, y, ne)
#     elif c=="R":
#         move(x + 1, y, ne)
#     elif c=="U":
#         move(x, y + 1, ne)
#     elif c=="D":
#         move(x, y - 1, ne)
#     else:
#         if x>0:
#             if t:
#
#
#         move(x - 1, y, ne)
#         move(x + 1, y, ne)
#         move(x, y + 1, ne)
#         move(x, y - 1, ne)
#
# if t:
#     print(min(t))
# else:
#     print(max(t))
#


