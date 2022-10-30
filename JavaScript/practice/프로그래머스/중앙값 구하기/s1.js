function solution(array) {
  array.sort(function(a, b) {
      return a - b 
  })
  let result = Math.floor(array.length / 2)
  return array[result]
}