from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
q = list()
parents = list(range(N))
total = 0

for i in range(N) :
    maps = input().strip()
    for j in range(N) :
        if maps[j] != '0' :
            if ord(maps[j]) >= ord('a') :
                cable = ord(maps[j]) - ord('a') + 1
            else :
                cable = ord(maps[j]) - ord('A') + 27
            heappush(q, (cable, i, j))
            total += cable

def find(a) :
    if a == parents[a] :
        return a

    parents[a] = find(parents[a])
    return parents[a]

def union(a, b) :
    if a < b :
        parents[b] = a
    else :
        parents[a] = b

cnt = N-1
while q and cnt :
    cable, a, b = heappop(q)
    a = find(a)
    b = find(b)
    if a != b :
        union(a, b)
        cnt -= 1
        total -= cable

for i in range(N) :
    find(i)
    
print(total if len(set(parents)) < 2 else -1)
