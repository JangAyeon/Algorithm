/**
 * @param {string} s
 * @return {string}
 */

const popString = (stack) => {
  let tmp = "";

  while (stack.length > 0) {
    const curr = stack.pop();
    if (curr == "[") {
      break;
    }
    tmp = curr + tmp;
  }

  return tmp;
};

const parseNumber = (stack) => {
  let number = "";

  // NaN일때 true를 뱉는다 따라서 NaN이 안나올떄까지 더해준다
  while (stack.length > 0) {
    const curr = stack.pop();
    //console.log(curr)
    if (Number.isNaN(Number(curr))) {
      //console.log("다시 넣기 끝", curr)
      stack.push(curr);
      break;
    }
    number = curr + number;
  }

  return Number(number);
};

var decodeString = function (s) {
  let answer = "";

  const stack = [];

  for (const char of s) {
    if (char !== "]") stack.push(char);
    else {
      // ]를 만났을 떄
      const tmp = popString(stack);
      const number = parseNumber(stack); // 숫자가 나옴

      const decode = tmp.repeat(number);
      stack.push(decode);
    }
  }

  return stack.join("");
};
