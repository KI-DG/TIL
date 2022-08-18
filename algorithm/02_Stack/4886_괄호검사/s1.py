import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    texts = input()
    stack = []
    answer = 1
    for text in texts:
        if text == '(' and text == '{':     # '('가 있으면 stack에 더해준다.
            stack.append(text)
        else:
            if not stack:  # stack이 비어 있으면 나와라
                break
            stack.pop()
    else:
        if not stack:
            answer = 0

    print(f"#{tc} {answer}")