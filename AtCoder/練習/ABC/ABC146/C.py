
a,b,x=map(int,input().split())
def binary_search(start,end):
    if end-start<=1:return start
    else:
        i=(start+end)//2
        s = a * (i) + b * len(str(i))
        if s<=x:return binary_search(i,end)
        else:return binary_search(start,i)
print(binary_search(0,10**9+1))
