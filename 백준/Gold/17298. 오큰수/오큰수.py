import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
_list = list(map(int, input().split()))
stack = []
answer = deque()

for i in range(n-1, -1, -1):
    if not stack:
        stack.append(_list[i])
        answer.appendleft(-1)
        continue

    if stack[-1] > _list[i]:
        answer.appendleft(stack[-1])
        stack.append(_list[i])
    else:
        while True:
            if not stack:
                answer.appendleft(-1)
                stack.append(_list[i])
                break
            num = stack.pop()
            if num > _list[i]:
                answer.appendleft(num)
                stack.append(num)
                stack.append(_list[i])
                break
print(*answer)