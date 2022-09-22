import sys

sys.stdin = open("input.txt")


def preorder(g):  # 전위 순회
    global answer_preorder
    if par_list[g] != '.':
        answer_preorder += par_list[g]   # visit(n)
        preorder(par_list.index(ch1[g]))
        preorder(par_list.index(ch2[g]))


def inorder(g):  # 중위 순회
    global answer_inorder
    if par_list[g] != '.':
        inorder(par_list.index(ch1[g]))
        answer_inorder += par_list[g]   # visit(n)
        inorder(par_list.index(ch2[g]))


def postorder(g):  # 후위 순회
    global answer_postorder
    if par_list[g] != '.':
        postorder(par_list.index(ch1[g]))
        postorder(par_list.index(ch2[g]))
        answer_postorder += par_list[g]    # visit(n)


n = int(input())    # 노드의 개수
par_list = ['.'] * (n + 1)     # 부모의 노드
ch1 = [0] * (n + 1)            # 자식 1의 노드
ch2 = [0] * (n + 1)            # 자식 2의 노드

for i in range(1, n+1):         # 반복문을 통해 수를 가지고 온다
    par, left, right = list(map(str, input().split()))
    par_list[i] = par
    ch1[i] = left
    ch2[i] = right

answer_preorder = ''
answer_inorder = ''
answer_postorder = ''

preorder(1)
print(answer_preorder)
inorder(1)
print(answer_inorder)
postorder(1)
print(answer_postorder)