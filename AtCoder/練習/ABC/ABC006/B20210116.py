
n=int(input())


if n==1 or n==2:
    print(0)
    exit()
if n==3:
    print(1)
    exit()

a,b,c=0,0,1
for i in range(4,n+1):
    new=(a+b+c)%10007
    a=b
    b=c
    c=new

print(c)


# def trib(n):
#     if memo[n] > 0:
#         return memo[n]
#     if n < 3 :
#         return 0
#     if n == 3:
#         return 1
#
#     return (trib(n-1)+trib(n-2)+trib(n-3))%10007
#
# print(trib(n))