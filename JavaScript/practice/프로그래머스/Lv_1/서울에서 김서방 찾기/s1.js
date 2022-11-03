function solution(seoul) {
  for (const [index, element] of seoul.entries())
    // python 에서 enumerate와 같은 역할을 하는 것 array.entries()
    if (element === 'Kim') {
      return `김서방은 ${index}에 있다`
    }
}