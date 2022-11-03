function solution(my_string) {
  let answer = []
  // 숫자만 나타내기
  for (let x of my_string) {
    if (!isNaN(x))
      answer.push(parseInt(x))
  }
  answer.sort()
  return answer
}