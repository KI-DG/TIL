import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    operator = list(input().split())
    arr = list(map(int, input().split()))
    operator_dic = {'+': operator[0], '-': operator[1], '*': operator[2], '/': operator[3]}
    