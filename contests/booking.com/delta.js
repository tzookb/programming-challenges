function delta_encode(array) {
    var res = []

    for (let i=0; i<array.length; i++) {
        let item = array[i]
        if (i===0) {
            res.push(item)
            continue
        }
        let prev = array[i-1]

        let diff = item - prev
        if (Math.abs(diff) >= 127) {
            res.push(-128);
        }
        res.push(diff)
    }
    return res
}

let res = delta_encode([
    25626,
    25757,
    24367,
    24267,
    16,
    100,
    2,
    7277
])

res = delta_encode([
1, 128
])

res.map(item=>console.log(item))