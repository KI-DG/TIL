function solution(n, k) {
  answer = n * 12000 + 2000 * (k - Math.floor(n / 10))
  return answer;
}