import sys

sys.stdin = open('input')

for tc in range(1, 11):
    n, numbers = input().split()
    n = int(n)
    stack = []
    numbers_str = list(str(numbers))

    for i in range(n):
        # 1. 만약 비어 있으면 그냥 넣고
        if not stack:
            stack.append(numbers_str[i])
        # 2. 있으면 마지막꺼랑 비교한후 같으면 빼주고
        else:
            if numbers_str[i] == stack[-1]:
                stack.pop()
        # 3. else: 다르면 다음것을 넣어줘라
            else:
                stack.append(numbers_str[i])

    print(f"#{tc}", end=' ')
    print(*stack, sep='')