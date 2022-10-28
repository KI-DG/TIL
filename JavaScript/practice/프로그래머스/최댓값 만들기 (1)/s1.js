function solution(numbers) {
  const sort_num = numbers.sort(function (a, b) {
    return a - b
  })

  let answer = sort_num[numbers.length - 1] * sort_num[numbers.length - 2]
  return answer;
}