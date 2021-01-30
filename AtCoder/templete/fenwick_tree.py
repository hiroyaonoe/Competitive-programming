
"""
長さNの配列に対し、
- 要素の1点変更
- 区間の要素の総和
をO(log N)で求めることが出来るデータ構造
https://atcoder.github.io/ac-library/document_ja/fenwicktree.html
"""
import typing

class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    # data[p] += x
    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    # sum(data[left:right])
    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self.sum(right) - self.sum(left)

    # sum(data[:right])
    def sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


# 長さnの数列aの転倒数s
tree=FenwickTree(n)

s=0
for i in range(n):
    s += i - tree.sum(a[i])
    tree.add(a[i],1)