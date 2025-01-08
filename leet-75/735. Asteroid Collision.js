/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function (asteroids) {
  const stack = [];
  while (asteroids.length > 0) {
    const num1 = asteroids.shift();
    if (stack.length == 0) {
      stack.push(num1);
    } else {
      // positive meaning right, negative meaning left
      const num2 = stack.pop();
      if (num1 < 0 && num2 > 0) {
        if (Math.abs(num1) < Math.abs(num2)) {
          stack.push(num2);
        } else if (Math.abs(num1) > Math.abs(num2)) {
          asteroids.unshift(num1);
        }
      } else {
        stack.push(num2);
        stack.push(num1);
      }
    }
    //console.log(asteroids, stack)
  }
  return stack;
};
