di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 3
M = 4
arr = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(N):
    for j in range(M):
        for d in range(1, 3):  # 위치먼저 두가지중 먼저나오면
            for k in range(4):  # 방향먼저
                ni = i + di[k] * d
                nj = j + dj[k] * d
                if 0 <= ni < N and 0 <= nj < M:
                    print(ni, nj)