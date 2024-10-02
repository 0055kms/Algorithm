import sys
input = sys.stdin.readline
from collections import defaultdict
dic = defaultdict(int)
cnt_all = 0
while True:
    name = input().rstrip()
    if name == '': break
    else:
        dic[name] += 1
        cnt_all += 1
A = list(dic.items())
A.sort(key = lambda x: x[0])
for name,cnt in A:
    print(f"{name} {cnt / cnt_all * 100:.4f}")