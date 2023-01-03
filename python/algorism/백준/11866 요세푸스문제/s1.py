from collections import deque

'''
7 3
'''
'''
<3, 6, 2, 7, 5, 1, 4>
'''

n, k = map(int, input().split())
s = deque([])

for i in range(1, n + 1):
    s.append(i)

print('<', end='')

while s:
    for i in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')

    if s:
        print(', ', end='')

print('>')
