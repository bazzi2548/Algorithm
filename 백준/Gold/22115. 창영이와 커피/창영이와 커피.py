import sys
input = sys.stdin.readline

n, k = map(int, input().split())
_list = list(map(int, input().split()))
dp = [int(1e9)] * (k+1)
dp[0] = 0
for C in _list:
    for i in range(k, C-1, -1):
        dp[i] = min(dp[i], dp[i-C]+1)

print(-1 if dp[k] > n else dp[k])