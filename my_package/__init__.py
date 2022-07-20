def solution(n, words):
    answer = []

    num = 0
    order = 1

    before_word = words[0][-1] #이전 단어 마지막 글자

    word_list = [words[0]] #단어 list

    for i, v in enumerate(words[1:]): #n번째 돌고 나면 차례 1증가
        if (i+2)%n == 1:
            order += 1

        next_word = v[0] # 다음 단어 마지막 글자

        if before_word != next_word or v in word_list:  #글자가 서로 안맞거나 이전에 있었던 단어일 경우
            answer.append(n if (i+2)%n == 0 else (i+2)%n)
            answer.append(order)
            break

        word_list.append(v) #단어 list에 추가

        before_word = v[-1]
    
    if len(answer) == 0:
        answer = [0,0]

    return answer

