n=int(input())

# def change(a):
#     moji=[]
#     ans=[]
#     for i in list(a):
#         if i not in moji:
#             moji.append(i)
#         code=moji.index(i)+97
#         ans.append(chr(code))
#     return "".join(ans)

ans=[[] for i in range(10)]


for i in range(n):
    if i==0:
        ans[i].append(["a",1])
    else:
        for moji,index in ans[i-1]:
            for plus in range(index):
                new=moji+chr(plus+97)
                ans[i].append([new,index])
            new=moji+chr(index+97)
            ans[i].append([new,index+1])

for a,b in ans[n-1]:
    print(a)