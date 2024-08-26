import sys
input = sys.stdin.readline

n=int(input())

def getNumber(n):
    res=''
    if n==0:
        print(0)
        return
    while n!=0:
        if n%(-2)!=0:
            res +='1'
            n=n//(-2)+1
        else:
            res +='0'
            n=n//(-2)
    
    print(res[::-1])

getNumber(n)