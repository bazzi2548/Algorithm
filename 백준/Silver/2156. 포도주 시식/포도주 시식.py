import sys

input = sys.stdin.readline

n = int(input())
_list = [int(input()) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(3)]
dp[1][1] = _list[0]

for i in range(1, n):
    dp[0][i + 1] = max(dp[0][i], dp[1][i], dp[2][i])
    dp[1][i + 1] = dp[0][i] + _list[i]
    dp[2][i + 1] = dp[1][i] + _list[i]

print(max(dp[0][-1], dp[1][-1], dp[2][-1]))