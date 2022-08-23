import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    word = input().split()
    result = ''
    stack = []
    is_error = False    # 에러가 나는지 안나는지 확인

    for char in word:
        if char not in '*/+-.':     # 연산자이거나 .이 아닐경우 push해준다.
            stack.append(int(char))
        else:
            if char == '.':     # .일경우 마지막이기 때문에 종료해줘야된다.
                break
            if len(stack) >= 2:     # 스택의 두개 이상일 경우에만 연산이 되기 때문에 스택은 최소 두개 여야 된다.
                x = stack.pop()
                y = stack.pop()

                if char == '+':
                    stack.append(y + x)
                elif char == '-':
                    stack.append(y - x)
                elif char == '*':
                    stack.append(y * x)
                elif char == '/':
                    stack.append(y // x)
            else:                   # 스택의 길이가 두개 보다 작았지만 아직 .이 나오지 않으면 오류가 난다.
                is_error = True
    if len(stack) != 1:      # 결과 값은 하나만 나와야 된다.(출력 시 스택엔 결과가 딱 하나만 존재해야 함!) 용준님 감사합니다.
        print(f'#{tc} error')
    elif is_error == True:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack[-1]}')


