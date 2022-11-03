function solution(num) {
  let answer = 0
  let number = num
  while (answer <= 500) {
    if (num === 1) {
      answer = 0
      break
    }
    if (answer === 500 && number != 1) {
      answer = -1
      break
    }
    if (number === 1) {
      break
    }
    if (number % 2 === 1) {
      answer += 1
      number = (number * 3) + 1
    } else {
      answer += 1
      number = Math.floor(number / 2)
    }
  }
  return answer
}