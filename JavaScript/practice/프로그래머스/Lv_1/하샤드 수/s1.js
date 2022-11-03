function solution(x) {
  let answer = true
  let sum_x = (x + '').split('')
  let n = 0
  for (let i = 0; i < sum_x.length; i++) {
    n += parseInt(sum_x[i])
  }
  if (x % n) {
    return answer = false
  } else {
    return answer
  }
}