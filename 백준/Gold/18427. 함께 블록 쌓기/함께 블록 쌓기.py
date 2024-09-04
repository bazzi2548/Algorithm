import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
dp = [[1]+[0]*h for i in range(n+1)]
for i in range(1, n+1):
    for j in range(h+1):
        dp[i][j] = dp[i-1][j]
    _list = list(map(int, input().split()))
    
    for number in _list:
        for j in range(number, h+1):
            dp[i][j]+=dp[i-1][j-number]

print(dp[n][h]%10007)