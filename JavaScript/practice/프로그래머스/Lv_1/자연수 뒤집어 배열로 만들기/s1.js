function solution(n) {
  const answer = []
  let strnumber = String(n).split('')
  // 문자열로 변경
  for (let i = strnumber.length - 1; i > -1; i--) {
    let n = parseInt(strnumber[i])
    // 문자열로 변경한것을 다시 정수로 변경
    answer.push(n)
    // 정수로 변경한 값을 빈 리스트에 넣어주기
  }

  return answer
}