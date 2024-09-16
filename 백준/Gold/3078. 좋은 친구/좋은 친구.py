import sys
input = sys.stdin.readline
from collections import defaultdict,deque
N,K = map(int,input().split())
stu = [input().rstrip() for _ in range(N)]
ans = 0
dict = defaultdict(int)
"""
(등수,이름길이) 크기 K 큐
넣을 때 정답,dict 업데이트
뺄 때 dict 업데이트
"""
q = deque()
for i in range(K):
    l = len(stu[i])
    q.append((i,l))
    ans += dict[l]
    dict[l] += 1

for i in range(K,N):
    l = len(stu[i])
    q.append((i,l))
    ans += dict[l]
    dict[l] += 1
    tmp_i,tmp_l = q.popleft()
    dict[tmp_l] -= 1
print(ans)