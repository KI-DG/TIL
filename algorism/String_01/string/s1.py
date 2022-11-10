import sys

sys.stdin = open("input.txt", "rt", encoding='UTF8')

for tc in range(1, 11):
    t = int(input())
    word = input()
    sentence = input()

    sentence_count = sentence.count(word)

    print(f"#{tc} {sentence_count}")
