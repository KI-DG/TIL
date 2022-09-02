import sys

sys.stdin = open('input')

n = input().replace('"', '')

x = n.split(',')

for i in range(len(x)):
    y = x[i]
    z = y.split()
    print(z)
    z_dict = {z[1]: z[2]}
    print(z_dict)

    if 'Enter' in z:
        print(f'"{z[2]}님이 들어왔습니다."')
    elif 'Change' in z:
        print(f'"{z[2]}님이 들어왔습니다."')






