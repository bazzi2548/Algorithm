import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    abP, bcP, caP = map(int, input().split())

    max_price = 0
    
    for ab_num in range(min(a, b) + 1):
        bc_num = min(b - ab_num, c)
        ca_num = min(c - bc_num, a - ab_num)
        
        max_price = max(max_price, ab_num * abP + bc_num * bcP + ca_num * caP)
        
        ca_num = min(c, a - ab_num)
        bc_num = min(b - ab_num, c - ca_num)
        
        max_price = max(max_price, ab_num * abP + bc_num * bcP + ca_num * caP)
    
    print(max_price)