import sys
input = sys.stdin.readline
N = int(input())
string = input().rstrip()
match = {}
for i in range(N):
    match[chr(65+i)] = int(input())

st = []
for c in string:
    if 'A'<=c<='Z':
        st.append(match[c])
    else:
        s,e = st.pop(),st.pop()
        if c == '*': e *= s
        if c == '+': e += s
        if c == '/': e /= s
        if c == '-': e -= s
        st.append(e)
print(f'{st[0]:.2f}')