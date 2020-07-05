function countingValleys(n, s) {
  const steps = s.split('');
  let level = 0;
  let isNewValley = false;
  let valleys = 0;

  steps.map(step => {
    level = step === 'U' ? level + 1 : level -1;
    if (level < 0 && !isNewValley) {
      isNewValley = true;
    }
    if (level === 0 && isNewValley) {
      isNewValley = false;
      valleys++;
    }
  })
  return valleys;
}

export default countingValleys;