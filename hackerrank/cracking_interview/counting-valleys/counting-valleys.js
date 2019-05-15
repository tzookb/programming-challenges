function countingValleys(n, s) {
    //dont care about "n"
    let level = 0;
    let valleys = 0;
    let isNewVally = false;

    s.split('').map(step => {
        level = step === 'U' ? level + 1 : level -1;
        if (level === -1 && !isNewVally) {
            isNewVally = true;
        }
        if (level === 0 && isNewVally) {
            isNewVally = false;
            valleys++;
        }
    })
    return valleys;
}
