// let str = 'ifailuhkqq'
let str = 'kkkk'
const gePossiblePairs = n => {
    if (n === 1) {
        return 0
    }
    if (n === 2) {
        return 1
    }
    let sum = 0;
    for (let i = 1; i < n; i++) {
        sum += i;
    }
    return sum;
}
function sherlockAndAnagrams(s) {
    let anagrams = 0
    const subs = {}
    for (let i = 0; i < s.length; i++) {
        for (let j = i; j < s.length; j++) {
            let sub = s.substring(i, j+1)
            sub = sub.split('').sort().join('')
            if (!(sub in subs)) {
                subs[sub] = []
            }
            subs[sub].push([i, j])
        }
    }

    for (let key in subs) {
        const subsetsCount = subs[key].length
        anagrams += gePossiblePairs(subsetsCount)
    }
    return anagrams
}

const res = sherlockAndAnagrams(str)
console.log(res)

