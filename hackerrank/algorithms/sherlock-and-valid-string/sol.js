
function isValid(s) {
  if (s.length <= 3) {
    return 'YES'
  }
  const charsCount = {}
  s.split('').map(c => {
      if (!(c in charsCount)) {
          charsCount[c] = 0
      }
      charsCount[c]++
  })

  return 'YES'
  return 'NO'
}

export default isValid