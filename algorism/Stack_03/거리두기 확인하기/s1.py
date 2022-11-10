
'''''
[["POOOP",
  "OXXOX",
  "OPXPX",
  "OOXOX",
  "POXXP"],
 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
 ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
 ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
'''''
dx = [-1, 1, 0, 0]   # 상 하 좌 우
dy = [0, 0, -1, 1]

#
# def dfs(places):
#     visited[i][j] =


for z in range(5):
    place = input()
    visited = [[False]*5 for _ in range(5)]
    result = 1

    for i in range(5):
        for j in range(5):
            if not visited[i][j] and place[i][j] == 'P':
                dfs()

