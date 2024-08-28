import sys
input = sys.stdin.readline

n, x = map(int, input().split())
answer = x - n
_list = ["A"] * n

def cal(idx):    
    for i in range(25, 0, -1):
        if answer - i >= 0:
            _list[idx] = chr(65+i)
            return i

def sol():
    global answer
    for i in range(n-1, -1, -1):
        if answer > 0:
            answer -= cal(i)
        
        if answer == 0:
            print(''.join(_list))
            return
    print("!")

sol()