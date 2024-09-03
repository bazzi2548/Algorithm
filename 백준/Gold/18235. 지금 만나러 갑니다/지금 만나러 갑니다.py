import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

n, a, b = map(int, input().split())
visit = defaultdict(set)

def bfs():
    q = deque()
    q.append((0, a, 0))
    q.append((0, b, 1))
    while q:
        day, now, duck = q.popleft()
        if duck and now in visit[day]:
            return day
        
        for next in (now + 2**day, now - 2**day):
            if 0 < next <= n:
                if not duck:
                    visit[day+1].add(next)
                q.append((day+1, next, duck))
    return -1

print(bfs())
