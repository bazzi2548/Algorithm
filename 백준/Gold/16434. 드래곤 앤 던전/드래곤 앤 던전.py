import sys
input = sys.stdin.readline

N, A = map(int, input().split())
_list = [list(map(int, input().split())) for _ in range(N)]

def check(damage, maxHP):
    curHP = maxHP
    for t, a, h in _list:
        if t == 1:
            turn = h//damage if not h % damage else h//damage+1
            curHP -= a * (turn-1)
        else:
            damage += a
            curHP += h
            if curHP > maxHP:
                curHP = maxHP
        if curHP <= 0:
            return False
    return True


result = 0
start, end = 1, N*int(1e12)
while start <= end:
    mid = (start+end)//2
    if check(A, mid):
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)