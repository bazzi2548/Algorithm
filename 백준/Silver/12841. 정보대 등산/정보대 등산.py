import sys
input = sys.stdin.readline

n = int(input())
_list = list(map(int, input().split()))
left = [0] + list(map(int, input().split()))
right = [0] + list(map(int, input().split()))
dp = [[int(1e9)] * n for _ in range(2)]
dp[0][0] = 0
dp[1][0] = _list[0]
crossPos = 0

for i in range(1, n):
    dp[0][i] = left[i] + dp[0][i-1]

    if dp[1][i-1] + right[i] > dp[0][i] + _list[i]:
        crossPos = i+1
        dp[1][i] = dp[0][i] + _list[i]
    else:
        dp[1][i] = dp[1][i-1] + right[i]

print(crossPos, dp[1][-1])