import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = Counter(a + b for a in A for b in B)

answer = 0
for c in C:
    for d in D:
        answer += AB.get(-(c + d), 0)

print(answer)
