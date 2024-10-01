import sys
input = sys.stdin.readline

def calculate(stack):
    answer = 0
    while stack:
        if stack[-1] == "{" and stack[-2] == "}":
            stack.pop()
            stack.pop()
            answer += 2
        elif stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 1
    return answer

cnt = 1
while True:
    stack = []
    string = list(map(str, input().strip()))

    if "-" in string:
        break
    
    for i in string:
        if i == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    
    if not stack:
        print(f"{cnt}. 0")
    else:
        print(f"{cnt}. {calculate(stack)}")
    cnt += 1