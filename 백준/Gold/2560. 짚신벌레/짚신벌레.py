import sys
input = sys.stdin.readline

a, b, d, N = map(int, input().split())
dp = [1]*a + [0]*(N + 1 - a)
answer = 0

for i in range(a, N+1):
    dp[i] = (dp[i-1] + dp[i-a]) % 1000
    if i >= b:
        dp[i] = (dp[i] - dp[i-b]) % 1000

answer = dp[N]
if N>=d:
    answer = (answer - dp[N - d]) % 1000

print(answer)