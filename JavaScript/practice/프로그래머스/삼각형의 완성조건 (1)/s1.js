function solution(sides) {
  var answer = 2;
  let max_side = Math.max(...sides)
  let sumsum = 0
  sides.forEach((item) => {
    sumsum += item
  })
  const side = sumsum - max_side
  if (side > max_side) {
    answer = 1
  } else {
    answer = 2
  }
  return answer;
}