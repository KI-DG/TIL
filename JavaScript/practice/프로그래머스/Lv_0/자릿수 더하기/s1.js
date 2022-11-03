function solution(n) {
  let answer = 0;
  n = n.toString()
  // 문자타입으로 변환
  for (let i = 0; i < n.length; i++) {
    answer += parseInt(n[i])
    // 정수로 다시 반환
  }
  return answer;
}