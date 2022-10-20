function solution(numbers) {
  const sum = numbers.reduce(function (answer, number) {
    return answer += number
  }, 0)
  return sum / numbers.length
}