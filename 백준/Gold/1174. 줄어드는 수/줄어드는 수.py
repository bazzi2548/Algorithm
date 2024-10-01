import sys
input = sys.stdin.readline

n = int(input())
number = []

def dfs(num, strNum):
    number.append(int(strNum))
    if num == 0:
        return
    
    for i in range(num-1, -1, -1):
        dfs(i, strNum+str(i))

for i in range(9, -1, -1):
    dfs(i, str(i))

number.sort()

print(number[n-1]) if n <= len(number) else print(-1)