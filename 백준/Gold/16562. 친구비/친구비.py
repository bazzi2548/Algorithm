import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
A_list = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]

def find(a):
    if parent[a] == a:
        return a  
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if A_list[a] > A_list[b]:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

_set = set()
cost = 0

for i in range(1, n+1):
    if find(i) not in _set:
        cost += A_list[parent[i]]
        _set.add(parent[i])

print("Oh no" if cost > k else cost)