import sys
input = sys.stdin.readline
N,H = map(int,input().split())
bot,top = [],[]
for i in range(N):
    if i % 2 == 0:
        bot.append(int(input())) # 0부터 k까지
    else:
        top.append(int(input())) # H-K부터 H까지
check = [0] * H # k~k+1 에 들어갈 때 장애물 수
for i,v in enumerate(top):
    top[i] = H-v
bot.sort()
top.sort()

cnt = len(bot)
for h in range(H):
    while top and top[0] <= h:
        cnt += 1; top.pop(0)
    while bot and bot[0] <= h:
        cnt -= 1; bot.pop(0)
    check[h] = cnt
tmp = min(check)
print(tmp,check.count(tmp))