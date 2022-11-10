n = int(input())
queue = list(range(1, n + 1))

while len(queue) > 1:
    queue.pop(0)
    queue.append(queue.pop(0))

print(queue[0])
# 시간 초과 난다. n = 500000이라 시간 복잡도에 의해 Fail이 난다.