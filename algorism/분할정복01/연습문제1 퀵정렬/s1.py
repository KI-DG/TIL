import sys

sys.stdin = open('input.txt')


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))
    quick_sort(data, 0, len(data) - 1)

    print(*data)