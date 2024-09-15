import sys
input = sys.stdin.readline
S = input().rstrip()
P = input().rstrip()
stack = []
for c in S:
    stack.append(c)
    l = len(stack)
    if l >= len(P):
        if stack[l-len(P):] == list(P):
            for _ in range(len(P)):
                stack.pop()
if not stack: print("FRULA")
else: print(''.join(stack))