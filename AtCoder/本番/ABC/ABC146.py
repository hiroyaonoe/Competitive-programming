# S=input()
# if S=="SUN":print("7")
# if S=="MON":print("6")
# if S=="TUE":print("5")
# if S=="WED":print("4")
# if S=="THU":print("3")
# if S=="FRI":print("2")
# if S=="SAT":print("1")

# N=int(input())
# S=list(input())
# ans=""
# for i in S:
#     neword=ord(i)+N
#     if neword>90:neword-=26
#     ans+=chr(neword)
# print(ans)

# A,B,X=map(int,input().split(" "))
# SS=X//A
# SS=min(SS,1000000000)
# ans=0
# for i in range(SS):
#     n=SS-i
#     if X>=A*(n)+B*len(str(n)):
#         ans=n
#         break
# print(ans)

N=int(input())-1
a=[]*N
b=[]*N
ansa=[]*N
ansb=[]*N
for i in range(N):
    a[i],b[i]=map(int,input().split(" "))
K=0
log=[{0}*(N+1)]
for i in range(N):
    still=True
    c = set(log[a[i]] + log[b[i]])
    for j in range(K):
        if j not in c:
            log[a[i]].append(j)
            log[b[i]].append(j)
            ansa=j
            still=False
            break
    if still:
        K+=1
        log[a[i]].append(K)
        log[b[i]].append(K)




    # for j in range(min(len(log[a[i]]),len(log[b[i]]))):
    #         if log[a[i]][j]<log[b[i]][j]:
    #             log[b[i]].append(log[a[i]])
    #             still=False
    #             break
    #         if log[b[i]][j]<log[a[i]][j]:
    #             log[a[i]].append(log[b[i]])
    #             still=False
    #             break
    # if still:
    #     if len(log[a[i]])<len(log[b[i]]):
    #         log[a[i]].append(log[b[i]][len(log[a[i]])])
    #     if len(log[b[i]])<len(log[a[i]]):
    #         log[b[i]].append(log[a[i]][len(log[b[i]])])
    #     if len