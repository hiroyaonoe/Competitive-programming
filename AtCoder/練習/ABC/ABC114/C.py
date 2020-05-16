# 解説AC

import sys
sys.setrecursionlimit(2000000)

n=int(input())
three=['3','5','7']


ans=[]
def search(dfs):
    newdfs=[]
    for moto in dfs:
        for i in three:
            new=moto+i
            threeok=[False for k in range(3)]
            if int(new)>n:
                print(len(ans))
                exit()
            for m in list(new):
                for j in range(3):
                    if m==three[j]:
                        threeok[j]=True
                        break
            if False not in threeok:
                ans.append(new)
            newdfs.append(new)
    search(newdfs)

search(three)




# ３進数にしたときの最上桁の扱いが不適
# def Base_10_to_n(X, n):
#     if (int(X/n)):
#         return Base_10_to_n(int(X/n), n)+str(X%n)
#     return str(X%n)
# ans=0
# m=1
# while True:
#     tm=Base_10_to_n(m,3)
#     tm='0'*(3-len(tm))+tm
#     threeok=[False for i in range(3)]
#     sft=[]
#     for i in list(tm):
#         for j in range(3):
#             if i==str(j):
#                 sft.append(three[j])
#                 threeok[j]=True
#                 break
#     mm=int(''.join(sft))
#     if mm>n:
#         break
#     if False not in threeok:
#         ans+=1
#     m+=1
#
# print(ans)





# それぞれ１回以上現れるの条件なしの場合
# while True:
#     ok=True
#     for i in list(str(n)):
#         if i not in three:
#             ok=False
#             break
#     if ok:
#         break
#     n-=1
#
# n=list(str(n))
# l=len(n)
# for i in range(l):
#     for j in range(3):
#         if n[i]==three[j]:
#             n[i]=str(j)
#             break
# n=''.join(n)
#
# ans=int(n,3)
#
# print(ans)





