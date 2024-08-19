import sys

input = sys.stdin.readline

N, K = map(int, input().split())
con = list(map(int, input().split()))
isRobot = [False] * (2 * N)
level = 1

while True:
    con = [con[-1]] + con[:-1]
    isRobot = [False] + isRobot[:-1]

    if isRobot[N - 1]:
        isRobot[N - 1] = False

    for i in range(N - 2, -1, -1):
        if isRobot[i] and not isRobot[i + 1] and con[i + 1] > 0:
            isRobot[i] = False
            isRobot[i + 1] = True
            con[i + 1] -= 1

    if isRobot[N - 1]:
        isRobot[N - 1] = False

    if con[0] > 0:
        isRobot[0] = True
        con[0] -= 1

    if con.count(0) >= K:
        break

    level += 1
print(level)
