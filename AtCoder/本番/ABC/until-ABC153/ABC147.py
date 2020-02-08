# a,b,c=map(int,input().split())
#
# if a+b+c>=22:print("bust")
# else:print("win")

# s=input()
# cnt=0
# for i in range(len(s)//2):
#     if s[i]!=s[-i-1]:cnt+=1
# print(cnt)

n=int(input())
aaa=[[] for _ in range(n)]
# ttt=[[] for _ in range(n)]
# fff=[[] for _ in range(n)]
for i in range(n):
    a=int(input())
    for j in range(a):
        x,y=map(int,input().split())
        aaa[i].append([x-1,y])
        # if y==1:ttt[x].append(i)
        # else:fff[x].append(i)



def search(human):
    global ans,cnt,truth
    if human<0:
        element = [2] * n
        for nin in truth:
            if nin == 1:
                for ele in aaa[nin]:
                    if element[ele[0]] != 2:
                        if element[ele[0]] != ele[1]: return
                    else:
                        element[ele[0]] = ele[1]

        ans = max(ans, cnt)
    else:
        search(human-1)
        truth[human]=1
        cnt+=1
        search(human-1)
    return


truth=[0]*n
ans=0
cnt=0
search(n-1)
print(ans)

