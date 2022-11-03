function solution(n) {
  let answer = 0
  let str_n = String(n).split('')

  for (let i = 0; i < str_n.length; i++) {
    let num_str_n = parseInt(str_n[i])
    answer += num_str_n
  }

  return answer
}