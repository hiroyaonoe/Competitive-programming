from heapq import *
def dijkstra(n, start, end, edge):
    """
    :param n: ノードの数
    :param start: 始点
    :param end: 終点
    :param edge: edge[a]は(b,l)の集合(b:aにつながる頂点 l:(a,b)の長さ)
    :return: startからendまでの最短距離
    """

    INF=1<<60
    d=[INF for i in range(n)]
    d[start]=0
    que=[]
    for i in range(n):
        heappush(que, (d[i], i))

    while que:
        key, v = heappop(que)
        if v==end:
            if d[end] == INF:
                print(-1)
            else:
                print(d[end])
        for (u,l) in edge[v]:
            if d[u]>d[v]+l:
                d[u]=l
                heappush(que, (d[u], u))
