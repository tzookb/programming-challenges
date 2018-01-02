function maxDifference(a) {
  let start = 0;
  let end = 0;
  let diff = 0;
  let found = false;

  for (let i=0; i<a.length; i++) {
    let cur = a[i];
    if (cur >= a[start] && i!=0) {
      console.log("skip:",i);
      continue;
    }
    for (let j=i+1; j<a.length; j++) {
      let next = a[j];
      let loopDiff = next - cur;
      if (loopDiff > diff) {
        diff = loopDiff;
        start = i;
        end = j;
        found = true;
      }
    }
  }
  // console.log("index:",start, end);

  if (found) {
    return diff;  
  }
  return -1;
}

let res = maxDifference([2,3,10,2,4,8,1]);
console.log(res);