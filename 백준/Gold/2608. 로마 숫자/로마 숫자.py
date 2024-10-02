import sys
input = sys.stdin.readline

r1 = input().rstrip()
r2 = input().rstrip()

roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roma2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
roma3 = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

def convert(string):
    res = 0
    i =0
    while i<len(string):
        if i+1 < len(string):
            if string[i:i+2] in roma2:
                res += roma2[string[i:i+2]]
                i+=2
                continue 

        if string[i] in roma:
            res += roma[string[i]]
            i+=1
    return res
    
def convert2(num): 
    tmp = "" 
    while num > 0: 
        for k,v in roma3.items():
            while num >= k:
                tmp += v 
                num -= k
    return tmp

answer = convert(r1) + convert(r2)
string = convert2(answer)
print(answer)
print(string)