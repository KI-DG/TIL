def solution(s):
    data = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]

    for i, v in enumerate(data):
        s = s.replace(v, data[i])

    return int(s)