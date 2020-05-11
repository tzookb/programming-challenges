
var hammingDistance = function(x, y) {
  let res = x ^ y
  let count = 0
  while (res) {
      count += res & 1
      res = res >> 1
  }
  return count 
};

console.log(hammingDistance(1,4));
