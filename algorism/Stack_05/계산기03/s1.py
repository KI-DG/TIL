import sys

sys.stdin = open('input')

for tc in range(1, 11):

    n = int(input())
    word = input()
    result = ''
    stack = []

    for token in word:
        # 토큰이 괄호이거나 연산자라면
        if token in '*/+-()':
            # 1) 스택이 비어 있는 상태이거나 토큰이 여는 괄호라면 push
            if not stack or token == '(':
                stack.append(token)
            # 2) 토큰이 연산자라면 스택중 제일 마지막 거랑 비교하여
            # 우선순위가 높으면 push 낮으면 더 우선순위가 낮은 연산자를 만날 때 까지 pop()
            elif token in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(token)
            elif token in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(token)
            # 3) 토큰이 닫는 괄호라면 여는 괄호를 만날때까지 pop 해준다.
            elif token == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()         # 여는 괄호하나를 버려준다.
        else:
            result += token
    while stack:
        result += stack.pop()
    for char in result:
        if char not in '*/+-':
            stack.append(int(char))
        else:
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(b + a)
            elif char == '-':
                stack.append(b - a)
            elif char == '*':
                stack.append(b * a)
            elif char == '/':
                stack.append(b / a)
    print(f'#{tc} {stack[-1]}')

