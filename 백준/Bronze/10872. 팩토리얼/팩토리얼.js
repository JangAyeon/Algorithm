const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
  });
  
rl.on("line" , (line) => {
   const N = Number(line.trim());
   // console.log(N);

    function cal(n){
        if(n<=1){return 1}
        else {return n*cal(n-1)}
    }
    console.log(cal(N))
   rl.close();
 });