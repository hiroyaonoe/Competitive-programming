# import numpy as np
#
# n=int(input())
# idx=np.arange(1,n+1)
# a=np.array(list(map(int,input().split())))
# ans=0
# for i in range(n):
#     minus=a[i]+i
#     mask = np.arange(n-minus)==a[minus:]
#     ans+=np.count_nonzero(mask)
#
# print(ans)


# import numpy as np
# cimport numpy as np
# cimport cython
# from libcpp cimport bool
#
# INT = np.int
# ctypedef np.int_t INT_t
# BOOL = np.bool
# ctypedef np.npy_bool BOOL_t
# def main():
#     cdef int n=int(input())
#     cdef str inn=input()
#     cdef np.ndarray[INT_t, ndim=1] a=np.array(list(map(int[:],inn.split())),dtype=INT)
#     cdef int ans=0
#     cdef int i
#     cdef int minus
#     cdef np.ndarray[BOOL_t, ndim=1] mask
#     for i in range(n):
#
#         minus=a[i]+i
#         mask = np.arange(n-minus,dtype=BOOL)==a[minus:]
#         ans += np.count_nonzero(mask)
#
#     print(ans)
#
# main()



import numpy as np

n=int(input())
idx=np.arange(1,n+1)
a=np.array(list(map(int,input().split())))
l=idx+a
r=idx-a
mi=max(l.min(),r.min())
ma=min(l.max(),r.max())
ans=0
for x in range(mi,ma+1):
    ll=np.count_nonzero(l==x)
    rr=np.count_nonzero(r==x)
    ans+=ll*rr

print(ans)

