function solution(n) {
  let answer = 0
  let num = n ** 0.5

  if (Number.isInteger(num) === true) {
    answer = (num + 1) ** 2
  } else {
    answer = -1
  }
  return answer
}