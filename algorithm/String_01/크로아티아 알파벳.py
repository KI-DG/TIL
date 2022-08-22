# replace 메서들 활용
# 두개짜리를 하나로 만들어 버린다.
word = input()
changes = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for change in changes:
    word = word.replace(change, ".")

print(len(word))

