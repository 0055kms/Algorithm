import sys
input = sys.stdin.readline
X = int(input())
level = 1
k = 1
while True:
    if k >= X:
        line = level
        mod = k-X+1
        break
    else:
        level += 1
        k += level
if level % 2 == 1: print(f'{mod}/{level-mod+1}')
else: print(f'{level-mod+1}/{mod}')
