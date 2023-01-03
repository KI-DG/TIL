n = int(input())
arr = [list(map(int, (input().split()))) for _ in range(n)]

answer = []

for i in range(n - 1):
    j = i + 1
    result = 0
    while j < n:
        if j + arr[i][0] > n:
            break
        elif j + arr[i][0] == n:
            result += arr[i][1]
            break
        elif arr[i + 1][0] != 1 and arr[i][1] < arr[i + 1][1] and arr[i + 1][0] + j == n - 1:
            result += arr[i + 1][1]
            break
        else:
            result += arr[i][1]

        j = i + arr[i][0]
        i = j

    answer.append(result)
print(max(answer))

'''
3
1 5
3 15
1 5

4
2 5
4 15
3 10
1 5
실패...
'''