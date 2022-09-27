import sys

sys.stdin = open('input.txt')


def partition(arr, left, right):
    pivot = arr[left]     # 기준점
    i, j = left, right

    while i <= j:           # while 문 시작 (왼쪽에서 시작하는게 오른쪽에서 시작하는것 보다 작을 떄)
        while i <= j and arr[i] <= pivot:     # 기준점보다 배열의 i의 값이 작을 때 i 의 값을 1 더해준다
            i += 1

        while i <= j and arr[j] >= pivot:     # 기준점보다 배열의 j의 값이 클때 j의 값을 1 빼준다
            j -= 1

        if i < j:                             # i 가 j 보다 작을 때 숫자를 바꿔준다
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]     # while 문을 빠져 나오면 기준점과 중간에 있는 값을 바꿔준다

    return j


def quick_sort(arr, left, right):             # 퀵 정렬
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    data = list(map(int, input().split()))

    quick_sort(data, 0, len(data) - 1)
    answer = data[int(n / 2)]         # 정수가 아닌 실수가 나와 int 를 써준다
    print(f'#{tc} {answer}')
