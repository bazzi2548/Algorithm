import sys

input = sys.stdin.readline

idxList = input().strip()
s1 = input().strip()
s2 = input().strip()

dp = [[[0] * 2 for _ in range(len(idxList))] for _ in range(len(s1))]
answer = 0

for i in range(len(s1)):
    if s1[i] == idxList[0]:
        dp[i][0][0] = 1
    if s2[i] == idxList[0]:
        dp[i][0][1] = 1
    
for i in range(len(s1)):
    for j in range(1, len(idxList)):
        if s1[i] == idxList[j]:
            for k in range(i):
                dp[i][j][0] += dp[k][j-1][1]
        
        if s2[i] == idxList[j]:
            for k in range(i):
                dp[i][j][1] += dp[k][j-1][0]

answer = 0
for i in range(len(s1)):
    answer += dp[i][len(idxList)-1][0] + dp[i][len(idxList)-1][1]

print(answer)
