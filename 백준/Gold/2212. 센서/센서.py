import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
sen = [x for x in map(int,input().split())]
sen.sort()
ar = []
for i in range(1,len(sen)):
    ar.append(sen[i]-sen[i-1])
ar.sort()
print(sum(ar[:len(ar)-K+1]))