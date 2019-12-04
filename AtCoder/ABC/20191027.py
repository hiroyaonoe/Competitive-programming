
# A,B = map(int,input().split(" "))
# if (A<=9)&(B<=9):
#     print(A*B)
# else:
#     print("-1")


# N=int(input())
# error=False
# for i in range(1,10):
#     for j in range(1,10):
#         if N==i*j:
#             error=True
# if error:
#     print("Yes")
# else:
#     print("No")


# import math
# n=int(input())
# ans=n
# i=1
# while(i<=math.sqrt(n)):
#     if n%i==0:
#         d=i+n/i-2
#         ans=min(ans,d)
#     i+=1
# print(int(ans))


# import math
# a,b,x=map(int,input().split(" "))
# if x>a**2*b/2:
#     V=a**2*b-x
#     L=2*V/(a**2)
#     print(math.degrees(math.atan(L/a)))
# else:
#     L=2*x/(a*b)
#     print(math.degrees(math.atan(b/L)))


