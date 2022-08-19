import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    texts = input()
    stack = []
    answer = 1
    for text in texts:
        if text == '(' or text == '{':     # '('가 있으면 stack에 더해준다.
            stack.append(text)

        elif text == ')':
            if not stack:       # ')' 가없으면 0 을 출력해주고 반복문을 나가준다.
                answer = 0
                break
            elif stack[-1] != '(':    # stack 마지막 원소가 '('가 아니면 0을 출력해준다.
                answer = 0
                break
            stack.pop()
        elif text == '}':
            if not stack:
                answer = 0
                break
            elif stack[-1] != '{':      # stack 마지막 원소가 '{'가 아니면 0을 출력해준다.
                answer = 0
                break
            stack.pop()

    if stack:
        answer = 0

    print(f"#{tc} {answer}")