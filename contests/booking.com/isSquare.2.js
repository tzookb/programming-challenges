
function polygon(a, b, c, d) {
    let sizes = [a,b,c,d];
    let sizesCount = {};
    
    sizes.map(item => {
        if ( !(item in sizesCount)) {
            sizesCount[item] = 0
        }
        sizesCount[item]++
    })
    
    if (Object.keys(sizesCount).length === 1) {
        return 2
    }
    
    console.log([3,4].indexOf(Object.keys(sizesCount).length))
    if ([3,4].indexOf(Object.keys(sizesCount).length) !== -1) {
        return 0
    }
    
    if (sizesCount[a] === 2) {
        return 1
    }
    return 0
}

console.log(polygon(36, 30, 36, 30));