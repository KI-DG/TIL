data = ["C", "A", "M","B","R","I","D","G","E"]

word = input()
for i in range(len(word)):
    if word[i] not in data:
        print(word[i], end="")

# KARIJERA

# 반복문을 어디에 돌릴까? replace 사용
# cambridge를 기준으로 사용해야 replace 사용가능
# word = input()

# for i in "CAMBRIDGE":
#   word = word.replace(i, '')

# print(word)