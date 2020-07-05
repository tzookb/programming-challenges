let a = [3, 4, 2, 1]

function minimumBribes(q) {
    //just check if valid first
    for (let i=0; i<q.length; i++) {
        const originalPos = q[i]
        const currentPos = i + 1
        if (currentPos + 2 < originalPos) {
            return console.log('Too chaotic');
        }
    }
    //now we know its valid, we should count bribes
    let bribes = 0
    for (let i=q.length-1; i>=0; i--) {
        const originalPos = q[i]
        let uptoPos = Math.max(0, originalPos - 1 - 2)
        while (uptoPos < i) {
            const valInPos = q[uptoPos]
            if (valInPos > originalPos) {
                bribes += 1
            }
            uptoPos++
        }
    }
    return console.log(bribes);
}

minimumBribes(a)
