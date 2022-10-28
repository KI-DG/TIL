function solution(money) {
  var answer = [];
  let cups = Math.floor(money / 5500)
  let change = money % 5500
  answer.push(cups, change)
  return answer;
}