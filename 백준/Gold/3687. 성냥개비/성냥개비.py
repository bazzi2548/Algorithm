import sys
input = sys.stdin.readline

INF = float('inf')
dp = [INF] * 101
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8


for i in range(8, 101):
    for j in range(2, i-1):
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i-j])))
        if j == 6 :
            dp[i] = min(dp[i], int(str(dp[i-j]) + '0'))

def getMax(n) -> int:
    if n % 2 == 1:
        return "7" + "1" * (n // 2 - 1)
    else:
        return "1" * (n // 2)

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n], getMax(n))
