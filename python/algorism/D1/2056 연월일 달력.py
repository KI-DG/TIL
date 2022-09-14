dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = int(input())
for tc in range(1, t + 1):
    a = input()

    if int(a[6:]) > dates[int(a[4:6])] or int(a[4:6]) < 1 or int(a[4:6]) > 12:
        print(f'#{tc} -1')
    else:
        year = a[0:4]
        month = a[4:6]
        date = a[6:8]

        print(f'#{tc} {year}/{month}/{date}')