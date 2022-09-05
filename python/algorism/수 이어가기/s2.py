n = int(input())

max_list = [n]

for i in range(n, 0, -1):
    result_list = [n, i]

    # for _ in range(n + 1):
    while True:
        next_num = n - i
        if next_num >= 0:
            result_list.append(next_num)
        else:
            break
        n = i
        i = next_num

    if len(max_list) < len(result_list):
        max_list = result_list

print(len(max_list))
print(*max_list)