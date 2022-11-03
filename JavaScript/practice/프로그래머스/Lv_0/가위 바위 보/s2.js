function solution(rsp) {
  let arr = {
    2: 0,
    0: 5,
    5: 2
  };
  const answer = [...rsp].map(v => arr[v]).join("");
  return answer;
}