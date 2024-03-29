import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t + 1):
    word = input()
    stack = []
    # calculator = {
    #     '+': lambda x, y: x + y,
    #     '-': lambda x, y: x - y,
    #     '*': lambda x, y: x * y,
    #     '/': lambda x, y: x / y
    # } 람다 함수를 이용해서 할 수도 있다.
    for char in word:
        # 1) 피연사자를 만나면 스택에 push 한다.
        if char not in '*/+-':
            stack.append(int(char))
        # 2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop 하여 연산하고,
        # 연산결과를 다시 스택에 push 한다.

        else:
            x = stack.pop()
            y = stack.pop()
            # stack.append(calculator[char](y,x))
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
        # 3) 수식이 끝나면, 마지막으로 스택을 pop 하여 출력한다.
    print(f'#{tc} {stack[-1]}')