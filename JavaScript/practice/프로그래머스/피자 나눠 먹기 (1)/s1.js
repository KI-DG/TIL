function solution(n) {
  var answer = 0;
  let pizza = Math.floor(n / 7)
  let pizza_count = n % 7
  if (pizza_count === 0) {
    answer = pizza
  } else {
    answer = pizza + 1
  }
  return answer;
}