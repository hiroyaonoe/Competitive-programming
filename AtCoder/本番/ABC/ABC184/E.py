h,w=list(map(int,input().split()))

a=[]# (w,h)

for i in range(h):
    aa=list(map(int,input().split()))
    a.append(aa)

from heapq import heapify, heappop, heappush, heappushpop

class PriorityQueue:
    def __init__(self, heap):
        '''
        heap ... list
        '''
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

d=[[10<<10 for i in range(w)] for j in range(w)]

