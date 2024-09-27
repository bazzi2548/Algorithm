import sys
input = sys.stdin.readline

N = int(input())
visit = [0] * (1000001)
_list = list(map(int, input().split()))
answer = 0
for i in _list:
    if not visit[i]:
        answer += 1
    else:
        visit[i] -= 1

    visit[i-1] += 1
print(answer)
