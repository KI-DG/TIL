import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    texts = input()
    stack = []

    for i in texts:

        # 1. 만약 비어 있으면 그냥 넣고
        if not stack:
            stack.append(i)
        # 2. 있으면 마지막꺼랑 비교한후 같으면 빼주고
        else:
            if i == stack[-1]:
                stack.pop()
        # 3. else: 다르면 다음것을 넣어줘라
            else:
                stack.append(i)

    print(f"#{tc} {len(stack)}")