n=int(input())
s=input()
l=len(s)

yet=True
i=0
while i<l:
    if s[i:i+3] == "fox":
        s=s[:i]+s[i+3:]
        l-=3
        i-=2
        # ii=i
        # while True:
        #     ii=s.find("fox",max(0,ii-2),min(l,ii+3))
        #     if ii!=-1:
        #         s=s[:ii]+s[ii+3:]
        #         l-=3
        #     else:
        #         break
    else:
        i+=1
print(l)
# from collections import deque
#
# l = deque()
# old=0
# for i in range(n):
#     if s[i]=="f":
#         l.append(i)
#
# yet=True
# while yet:
#     yet = False
#     newl=deque()
#     mi = 0
#
#     while len(l)>0:
#         i=l.popleft()
#         if s[i-mi:i+3-mi] == "fox":
#             yet = True
#             mi+=3
#             s=



