const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(line.trim());

  if (input.length == Number(input[0]) + 2) {
    rl.close();
  }
});

rl.on("close", () => {
  // N : 필요한 기능의 갯수
  const N = Number(input[0]);

  // 현재 시각 currHour시 currMin분
  // 공백으로 입력 나누고 각 요소에 Number로 형변환
  const [currHour, currMin] = input[1].split(" ").map(Number);

  // input의 2번째 요소부터는 기능 개발에 소요되는 분 값
  // 요소 한개씩 currValue로 받아 Number로 형변환하고
  // temp에 누적합 받아서
  // minutes 값으로 반환
  const minutes = input.slice(2).reduce((temp, currValue) => {
    return temp + Number(currValue);
  }, 0);

  // minSum은 기존 분 + 기능 개발 총 소요 분
  const minSum = currMin + minutes;

  // 60으로 나눈 나머지가 최종 분
  const min = minSum % 60;

  // 총 시간 = 60으로 나눈 몫 + 기존 시간
  // 시간은 24시간 단위 임으로 총 시간을 24로 나눈 나머지
  const hour = (currHour + Math.floor(minSum / 60)) % 24;
  console.log(hour, min);
});
