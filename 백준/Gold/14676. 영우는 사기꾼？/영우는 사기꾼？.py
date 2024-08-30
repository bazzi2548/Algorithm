import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
_list = [[] for _ in range(n+1)]
indegree=[0] * (n + 1)
built= [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    _list[x].append(y)
    indegree[y] += 1

def gameStart():
    for _ in range(k):
        a, b = map(int, input().split())
        if a == 1:
            if indegree[b]:
                print("Lier!")
                return
            
            if not built[b]:
                for i in _list[b]:
                    indegree[i] -= 1
            built[b] += 1
        else:
            if built[b] <= 0:
                print("Lier!")
                return
            
            built[b] -= 1
            if built[b] == 0:
                for i in _list[b]:
                    indegree[i] += 1
                    
    print("King-God-Emperor")

gameStart()