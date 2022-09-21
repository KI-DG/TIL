def selection_sort(i):
    if i == len(numbers) - 1:  # 종료 조건(마지막 원소일 때는 더이상 정렬할 필요가 없으므로 재귀 종료)
        return

    min_index = i  # 정렬되지 않는 부분 중 맨 앞 인덱스로 초기화

    for j in range(i + 1, len(numbers)):   # 맨 앞 인덱스 + 1부터 비교하여 최소값 인덱스 찾기
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    # 최소값과 자리를 바꿔준다
    selection_sort(i + 1)  # 재귀 호출


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(0)

print(numbers)