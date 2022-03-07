// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  let stack = [];
  let chars = S.split(" ");
  let MAX = Math.pow(2, 20);
  let MIN = 0;

  if (S.length > 2000 && S.length < 1) {
    return -1;
  }

  for (let i in chars) {
    if (
      !isNaN(chars[i]) &&
      parseInt(chars[i]) >= MIN &&
      parseInt(chars[i]) < MAX
    ) {
      stack.push(parseInt(chars[i]));
    }

    if (chars[i] == "POP" && stack.length > 0) {
      stack.pop();
    } else if (chars[i] == "POP" && stack.length == 0) {
      return -1;
    }

    if (chars[i] == "DUP" && stack.length > 0) {
      stack.push(stack[stack.length - 1]);
    } else if (chars[i] == "DUP" && stack.length == 0) {
      return -1;
    }

    if (chars[i] == "+" && stack.length >= 2) {
      let a = stack.pop();
      let b = stack.pop();
      if (a + b > MAX - 1) {
        return -1;
      } else {
        stack.push(a + b);
      }
    } else if (chars[i] == "+" && stack.length < 2) {
      return -1;
    }

    if (chars[i] == "-" && stack.length >= 2) {
      let a = stack.pop();
      let b = stack.pop();
      if (a - b < MIN) {
        return -1;
      } else {
        stack.push(a - b);
      }
    } else if (chars[i] == "-" && stack.length < 2) {
      return -1;
    }
  }

  if (stack.length < 1) {
    return -1;
  } else {
    return stack.pop();
  }
}
