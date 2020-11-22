a,b,c=list(map(int,input().split()))

dp=[[[-1 for i in range(101)] for j in range(101)] for k in range(101)]

def search(aa,bb,cc):
    if aa==100 or bb==100 or cc==100:
        dp[aa][bb][cc]=0

    i=dp[aa][bb][cc]
    if i != -1:
        return i

    m=aa+bb+cc
    i = 1 + search(aa+1,bb,cc) * (aa / m) + search(aa,bb+1,cc) * (bb / m) + search(aa,bb,cc+1) * (cc / m)
    dp[aa][bb][cc]=i

    return i

print(search(a,b,c))

# from collections import deque
# q=deque([(1,0,0),(0,1,0),(0,0,1)])
# while len(q)>0:
#     aa,bb,cc=q.popleft()
#
#     dp[aa + 1][bb][cc] = dp[aa][bb][cc] * (aa / (aa + bb + cc))
#     dp[aa][bb + 1][cc] = dp[aa][bb][cc] * (bb / (aa + bb + cc))
#     dp[aa][bb][cc + 1] = dp[aa][bb][cc] * (cc / (aa + bb + cc))
#
#     q.append((aa + 1, bb, cc))
#     q.append((aa, bb + 1, cc))
#     q.append((aa, bb, cc + 1))
#



# ma=a+b+c
# for m in range(1,ma+1):
#     for aa in range(1,min(a+1,m+1)):
#         for bb in range(max(1,m-aa-c),min(b+1,m-aa+1)):
#             cc=m-aa-bb
#
#             dp[aa][bb][cc]=dp[aa - 1][bb][cc]*(aa/m)+dp[aa][bb - 1][cc]*(bb/m)+dp[aa][bb][cc - 1]*(cc/m)
#             print(dp[aa][bb][cc])
#
#             # if (a == aa) and (b == bb) and (c == cc):
#             #     print(dp[a][b][c])
#             #     exit()

# print(dp[a][b][c])
# from collections import deque
# q=deque([(1,0,0),(0,1,0),(0,0,1)])

# ma=a+b+c
# for m in range(1,ma+1):
#     for i in range(max(100,m+1)):
#         aa=i
#         for j in range(max(100,m-i+1)):
#             bb=j
#             cc=m-j
#             if cc>=100:
#                 break
#
#             dp[aa + 1][bb][cc] = dp[aa][bb][cc] * (aa / (aa + bb + cc))
#             dp[aa][bb + 1][cc] = dp[aa][bb][cc] * (bb / (aa + bb + cc))
#             dp[aa][bb][cc + 1] = dp[aa][bb][cc] * (cc / (aa + bb + cc))
#
#             if (a == aa) and (b == bb) and (c == cc):
#                 print(dp[a][b][c])
#                 exit()
# print(dp[a][b][c])
# while len(q)>0:
#     aa,bb,cc=q.popleft()
#
#     dp[aa + 1][bb][cc] = dp[aa][bb][cc] * (aa / (aa + bb + cc))
#     dp[aa][bb + 1][cc] = dp[aa][bb][cc] * (bb / (aa + bb + cc))
#     dp[aa][bb][cc + 1] = dp[aa][bb][cc] * (cc / (aa + bb + cc))
#
#     q.append((aa + 1, bb, cc))
#     q.append((aa, bb + 1, cc))
#     q.append((aa, bb, cc + 1))
#
#     if (a==aa)and(b==bb)and(c==cc):
#         break
#
# print(dp[a][b][c])



