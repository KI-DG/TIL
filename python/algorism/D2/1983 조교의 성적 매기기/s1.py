import sys

sys.stdin = open("input.txt")

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    answer = []
    for i in range(n):
        mid, final, homework = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + homework * 0.2   # 중간 35% 기말 45% 과제 20%
        answer.append(total)

    score = answer[k - 1]  # k번째 값을 저장하는 변수

    answer.sort(reverse=True)  # 역순으로 정렬해줘서 제일 높은 값이 앞으로 오게 한다
    div = n // 10   # n은 10dml 배수 이므로 비율을 정하기 위해
    idx = answer.index(score)//div  # 몇번쨰 있는지 알아보기 위해서
    result = grade[idx]

    print(f'#{tc} {result}')
