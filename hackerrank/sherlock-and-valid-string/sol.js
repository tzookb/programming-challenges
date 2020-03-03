
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
  const occurences = {}
  Object.values(charsCount).map(oc => {
    if (!(oc in occurences)) {
      occurences[oc] = 0
    }
    occurences[oc]++
  })
  const occurencesCount = Object.keys(occurences).length
  if (occurencesCount > 2) {
    return 'NO'
  }
  if (occurencesCount == 1) {
    return 'YES'
  }
  if ('1' in occurences && occurences['1'] == 1) {
    return 'YES'
  }
  const [fkey, skey] = Object.keys(occurences)
  if (Math.abs(parseInt(fkey)-parseInt(skey)) == 1) {
    const max = Math.max(parseInt(fkey), parseInt(skey))
    if (occurences[max+''] == 1) {
      return 'YES'
    }
  }
  return 'NO'
}

const res = isValid('aaaabbcc')
console.log(res)

// export default isValid