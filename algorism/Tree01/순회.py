'''
정점 번호 1 ~ (E + 1)
간선 수
부모 - 자식 순
4
1 2 1 3 3 4 3 5
'''


def f(n):           # golbal cnt 없이 순회한 정점 수를 리턴하는 함수 L + R + V
    if n == 0:  # 서브트리가 비어있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1


def find_root(v):
    for x in range(1, v + 1):
        if par[x] == 0:  # 부모가 없으면 root
            return x


def preorder(n):  # 전위 순회
    if n:
        print(n)  # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):  # 중위 순회
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])


def postorder(n):  # 후위 순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)


E = int(input())  # 간선의 개수
arr = list(map(int, input().split()))
V = E + 1  # 정점의 개수
# 부모를 인덱스로 자식 번호 저장
# root = 1
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0] * (V + 1)

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
# for j in range(0, E * 2, 2):  # 위에랑 똑같음
#     p, c = arr[j], arr[j + 1]
    if ch1[p] == 0:  # 아직 자식이 없으면
        ch1[p] = c   # 자식 1로 저장
    else:
        ch2[p] = c   # 자식 2로 저장
    par[c] = p
root = find_root(V)
# print(root)
# print(ch1, ch2)
# preorder(root)
# inorder(root)
# postorder(root)
print(inorder(root))

