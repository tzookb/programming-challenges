
function polygon(a, b, c, d) {
    let sizes = [a,b,c,d];
    let sizesCount = {};
    
    for(let i=0; i<sizes.length; i++) {
        if (sizes[i] <= 0) {
            return 0
        }
        if ( !(sizes[i] in sizesCount)) {
            sizesCount[sizes[i]] = 0
        }
        sizesCount[sizes[i]]++
    }
    
    if (Object.keys(sizesCount).length === 1) {
        return 2
    }
    
    if ([3,4].indexOf(Object.keys(sizesCount).length) !== -1) {
        return 0
    }
    
    if (sizesCount[a] === 2) {
        return 1
    }
    return 0
}