import sys
from itertools import combinations as cb
input = sys.stdin.readline
while True:
    nums = [*map(int,input().split())]
    if nums == [0]: break
    else: nums = nums[1:]; nums = sorted(nums)
    for ar in cb(nums,6):
        print(*ar)
    print()