import sys
input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))
stacks = [[] for _ in range(4)]

def makeStacks():
    idx = 0
    for num in _list:
        if idx == 0:
            stacks[idx].append(num)
            idx += 1
            continue

        check = False
        for i in range(idx):
            if stacks[i][-1] < num:
                stacks[i].append(num)
                check = True
                break
        
        if not check:
            if idx == 4:
                return False
            stacks[idx].append(num)
            idx += 1

    return True

print("YES") if makeStacks() else print("NO")