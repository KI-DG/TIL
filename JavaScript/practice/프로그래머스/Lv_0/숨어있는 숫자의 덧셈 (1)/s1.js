function solution(my_string) {
  let answer = ''
  for (let x of my_string) {
    if (!isNaN(x)) {
      answer += x
    }
  }
  // 숫자만 추출
  let n = answer.toString()
  result = 0
  // 문자타입으로 변환
  for (let i = 0; i < n.length; i++) {
    result += parseInt(n[i])
    // 정수로 다시 반환
  }
  return result
}