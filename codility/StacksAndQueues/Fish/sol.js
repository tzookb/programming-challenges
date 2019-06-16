const Stack = require('./stack');

function solution(A, B) {
  const ups = new Stack();
  let survived = 0;

  A.map((fish, idx) => {
    const direction = B[idx];
    if (direction === 1) {
      ups.push(fish)
    } else {
      let eaten = false;
      while (ups.size()) {
        const upFish = ups.pop();
        if (upFish > fish) {
          ups.push(upFish);
          eaten = true;
          break;
        }
      }
      if (!eaten) {
        survived++;
      }
    }
  })
  return survived + ups.size();
}

const fish = [4,3,2,1,5];
const direction = [0,1,0,0,0];

const res = solution(fish, direction);
console.log(res);


// console.log(res);
