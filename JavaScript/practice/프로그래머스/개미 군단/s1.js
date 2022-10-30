function solution(hp) {
  let answer = 0
  let general = Math.floor(hp / 5)
  let soldier = Math.floor((hp - (general * 5)) / 3)
  let work = (hp - (general * 5)) % 3
  answer = general + soldier + work
  return answer
}