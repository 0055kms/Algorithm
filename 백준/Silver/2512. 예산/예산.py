import sys
from math import ceil

input = sys.stdin.readline
N = int(input())
ar = [x for x in map(int, input().split())]
all = int(input())

s, e = 0, max(ar)
while s <= e:
    m = (s + e) // 2
    get = 0
    for i in ar:
        if i > m:
            get += m
        else:
            get += i
    if get > all:
        e = m - 1
    else:
        s = m + 1

print(e)
