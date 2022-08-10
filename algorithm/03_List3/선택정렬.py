arr = [7, 2, 5, 3, 4, 6]
N = len(arr)

for i in range(N-1):
    min_index = i  # 구간의 맨 앞을 최소값으로 가정
    for j in range(i+1, N): # 실제 최소값 인덱스 찾기
        if arr[min_index] > arr[j]:
            min_index = j

    arr[min_index], arr[i] = arr[i], arr[min_index]

print(arr)