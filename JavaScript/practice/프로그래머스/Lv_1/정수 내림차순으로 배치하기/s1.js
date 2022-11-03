function solution(n) {
  let answer = 0
  let str_n = (n + '').split('')
  str_n.sort(function (a, b) {
    return b - a
  })
  answer = parseInt(str_n.join(''))
  return answer
}