const readline = require("readline");
let rl = readline.createInterface({
  input:process.stdin,
  output:process.stdout,
})

// 입력되는 모든 데이터를 가지고 있을 input 리스트
let input = [];

// readline 모듈의 on 메소드 사용해 입력 받음 
rl.on("line", (line)=>{
  // 입력되는 문자열의 공백 단위로 나누고 숫자형 변환해 한개씩 리스트 저장
  input.push(line.split(" ").map(Number));
  // line 이벤트는 rl.close() 만나기 전까지 실행됨
  // 입력 받는 기준은 ENTER(줄바꿈)임
  // 문제에서 들어오는 입력은 1줄임 
  if(input.length==1){
    // 입력 종료
    // line 이벤트 종료됨 
    rl.close(); // close 이벤트 실행됨
  }
})

// close 이벤트 핸들러 코드
rl.on("close",()=>{
  const [W, R] =input[0];

  // Math.trunc 사용해 소수접 이하 값 버림
  const answer = Math.trunc(W*(1+R/30));
  console.log(answer);
  rl.close();
})