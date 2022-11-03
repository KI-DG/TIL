function solution(arr) {

  const average = array => array.reduce((a, b) => a + b, 0) / array.length
  let answer = average(arr)
  return answer
}