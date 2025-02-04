const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];

rl.on("line", (line) => {
  lines.push(line.trim());
}).on("close", () => {
  const N = Number(lines[0]);
  let lectures = lines.slice(1).map((e) => e.split(" ").map(Number));
  const schedules = [];

  // 강의 시작과 종료를 별도로 저장
  lectures.forEach((lecture) => {
    schedules.push({ time: lecture[0], start: 1 });
    schedules.push({ time: lecture[1], start: -1 });
  });

  // 정렬: 시간이 같으면 종료(-1)가 먼저 오도록
  schedules.sort((a, b) =>
    a.time === b.time ? a.start - b.start : a.time - b.time
  );

  let cnt = 0;
  let answer = 0;

  schedules.forEach((schedule) => {
    if (schedule.start === 1) {
      cnt++; // 강의 시작 -> 강의실 사용 증가
    } else {
      cnt--; // 강의 종료 -> 강의실 사용 감소
    }
    answer = Math.max(answer, cnt); // 최댓값 갱신
  });

  console.log(answer);
});
