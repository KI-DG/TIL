function solution(my_string) {
  let answer = ''
  const collection = ['a', 'e', 'i', 'o', 'u']
  for (string of my_string) {
    if (collection.includes(string) === false) {
      answer += string
    }
  }
  return answer
}