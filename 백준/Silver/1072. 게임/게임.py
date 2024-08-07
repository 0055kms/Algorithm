import sys
input = sys.stdin.readline
X,Y = map(int,input().split())
cur = int(Y*100/X)
nxt = cur + 1
if cur == 99 or cur == 100: print(-1); sys.exit();
s, e = 0, 100000000000
while s <= e:
    m = (s + e)//2
    get = int((m+Y)*100/(m+X))
    if get>=nxt: e = m-1
    else: s = m+1
print(s)