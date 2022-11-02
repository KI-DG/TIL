function solution(array) {
  let answer = 0
  let array_str = array.toString()
  for (let arr of array_str) {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === '7') {
        answer += 1
      }
    }
  }
  return answer
}