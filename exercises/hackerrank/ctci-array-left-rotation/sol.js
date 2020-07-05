function rotLeft(a, n) {
  const arrLen = a.length;
  const minRotate = n % arrLen;
  return [
    ...a.slice(minRotate, arrLen),
    ...a.slice(0, minRotate)
  ]
}

const res = rotLeft([1,2,3,4,5], 5002)
console.log(res);
