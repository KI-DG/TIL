import sys

sys.stdin = open("input")


for tc in range(1, 11):
    n = int(input())
    word = input()  # 중위 표기법
    result = ''     # 후위표기법 변환 결과값
    stack = []      # 후위표기법으로 변환할때 연산자 저장
    stack_2 = []    # 피연산자 저장

    for token in word:
        # 토큰이 연산자일 때
        if token in '*+':
            # 1) 스택이 비어잇는 상태이거나 토큰이 여는 괄호라면 push
            if not stack:
                stack.append(token)
                # 2) 토큰이 연산자라면 스택 top과 비교하여 우선순위가 높으면 push
                # 낮으면 더 우선순위가 낮은 연산자를 만날 때까지 pop 하고 결과 값에 담음
            elif token == '*':
                while stack and stack[-1] in '*':
                    result += stack.pop()
                stack.append(token)  # 이후 스택에 연산자 push
            elif token in '+':
                while stack:
                    result += stack.pop()
                stack.append(token)  # 이후 스택에 연산자 push
            # 3) 토큰이 닫는 괄호라면 여는 괄호를 만날 때까지 모두 pop 하고 결과 값에 담음
        # 토큰이 피연산자라면 그대로 결과 값에 담음
        else:
            result += token
        # 혹시나 스택에 토큰이 남아있다면 모두 결과 값에 담음
    while stack:
        result += stack.pop()

    for char in result:
        # 1) 피연사자를 만나면 스택에 push 한다.
        if char not in '*+':
            stack_2.append(int(char))
        # 2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop 하여 연산하고,
        # 연산결과를 다시 스택에 push 한다.
        else:
            x = stack_2.pop()
            y = stack_2.pop()
            if char == '+':
                stack_2.append(y + x)
            elif char == '*':
                stack_2.append(y * x)

    print(f'#{tc} {stack_2[-1]}')