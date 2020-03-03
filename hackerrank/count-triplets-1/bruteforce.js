// let str = 'ifailuhkqq'
let arr = [1, 5, 5, 25, 125]
let r = 5

function countTriplets(arr, r) {
    let count = 0
    for (let i=0; i<arr.length; i++) {
        const optionals = {}
        const starter = arr[i]
        for (let j=i+1; j<arr.length; j++) {
            const middleItem = arr[j]
            if (middleItem/starter != r) {
                continue
            }
            for (let k=j+1; k<arr.length; k++) {
                const thirdItem = arr[k]
                if (thirdItem/middleItem == r) {
                    count++
                }
            }
        }
    }
    return count
}

const res = countTriplets(arr, r)
console.log(res)

