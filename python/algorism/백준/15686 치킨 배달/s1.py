n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
# 치킨 집과 집의 위치 저장
home_count = 0
chicken_count = 0

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
            home_count += 1
        elif city[i][j] == 2:
            chicken.append([i, j])
            chicken_count += 1

result = 0
if m == chicken_count:
    for x in range(home_count):
        answer = []
        for y in range(chicken_count):
            answer.append(abs(home[x][0] - chicken[y][0]) + abs(home[x][1] - chicken[y][1]))
        result += min(answer)
else:
    answer_result = []
    for x in range(home_count):
        answer = []
        for y in range(chicken_count):
            answer.append(abs(home[x][0] - chicken[y][0]) + abs(home[x][1] - chicken[y][1]))
        answer_result.append(sum(answer))
        print(answer)
    answer_result.sort()
    if m == 1:
        result = min(answer_result)
    else:
        for z in range(m):
            pass

print(result)
