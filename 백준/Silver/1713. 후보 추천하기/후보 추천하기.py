import sys
input = sys.stdin.readline
N = int(input())
l = int(input())
A = [int(x) for x in map(int,input().split())]
# [학생번호,게시하고 지난 시간,추천 횟수]
tools = []
for i in A:
    isIn = False
    for idx,val in enumerate(tools):
        if val[0] == i:
            isIn = True
            tools[idx][2] += 1
    if not isIn:
        if len(tools) < N:
            tools.append([i,0,1])
        else:
            tools.sort(key = lambda x: (-x[2],x[1]))
            tools[-1] = [i,0,1]

    for j in range(len(tools)):
        tools[j][1] += 1
tools.sort(key = lambda x: x[0])
ans = [x[0] for x in tools]
print(*ans)