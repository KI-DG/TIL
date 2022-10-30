function solution(n) {
  let answer = 2
  for (let i = 0; i <= Math.floor(n / 2); i++) {
      if (i * i === n) {
          answer = 1
          break
      } else {
          answer = 2
      }
  }
  return answer
}