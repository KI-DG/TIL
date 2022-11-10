t = int(input())

for tc in range(1, t + 1):
   test_case, n = input().split()  # test_case
   numbers = list(map(str, input().split()))  # 문자들이 들어있는 리스트

   data = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

   for i, v in enumerate(data):
        data[i] = i
   # data를 숫자로 변환
   for y, x in enumerate(numbers):
        if x == "ZRO":
            numbers[y] = 0
        elif x == "ONE":
            numbers[y] = 1
        elif x == "TWO":
            numbers[y] = 2
        elif x == "THR":
            numbers[y] = 3
        elif x == "FOR":
            numbers[y] = 4
        elif x == "FIV":
            numbers[y] = 5
        elif x == "SIX":
            numbers[y] = 6
        elif x == "SVN":
            numbers[y] = 7
        elif x == "EGT":
            numbers[y] = 8
        else:
            numbers[y] = 9
   # numbers data를 통해 숫자로 변경
   numbers.sort()
   # 숫자를 정렬

   for y, x in enumerate(numbers):
       if x == 0:
           numbers[y] = "ZRO"
       elif x == 1:
           numbers[y] = "ONE"
       elif x == 2:
           numbers[y] = "TWO"
       elif x == 3:
           numbers[y] = "THR"
       elif x == 4:
           numbers[y] = "FOR"
       elif x == 5:
           numbers[y] = "FIV"
       elif x == 6:
           numbers[y] = "SIX"
       elif x == 7:
           numbers[y] = "SVN"
       elif x == 8:
           numbers[y] = "EGT"
       else:
           numbers[y] = "NIN"
   # 정렬 된 숫자를 다시 문자로 변경

   print(f"#{tc}")
   print(*numbers)
