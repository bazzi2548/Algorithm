import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_set = set(map(int, input().split()))
answer = int(1e9)

for i in range(1, 1002):
    if i in _set: continue
    for j in range(1, 1002):
        if j in _set: continue
        for k in range(1, 1002):
            if k in _set: continue
            q = (i * j * k)
            if abs(N - q) < answer: answer = abs(N - q)
            if N + 1 < q: break

print(answer)
