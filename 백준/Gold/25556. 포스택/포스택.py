import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))
stacks = [[] for _ in range(4)]

def makeStacks():
    idx = 0
    for num in _list:
        if idx == 0:
            stacks[idx].append(num)
            idx += 1
            continue

        check = False
        for i in range(idx):
            if stacks[i][-1] < num:
                stacks[i].append(num)
                check = True
                break
        
        if not check:
            if idx == 4:
                print("NO")
                return False
            stacks[idx].append(num)
            idx += 1
    return True

def getAnswer():
    q = deque()
    while len(q) < N:
        idx = -1; num = -1
        for i in range(4):
            if stacks[i]:
                if num < stacks[i][-1]:
                    idx = i
                    num = stacks[i][-1]
    
        q.appendleft(stacks[idx].pop())
    for i in range(1, N):
        if q[i-1] >= q[i]:
            print("NO")
            return
        
    print("YES")

if makeStacks():
    getAnswer()