let a = [1, 3, 5, 2, 4, 6, 7]

function minimumSwaps(arr) {
    let swaps = 0
    for (let i=0; i< arr.length; i++) {
        const supposedVal = i + 1
        const currentVal = arr[i]
        if (supposedVal === currentVal) {
            continue
        }
        const tempVal = arr[currentVal-1]
        arr[currentVal-1] = currentVal
        arr[i] = tempVal
        i--
        swaps++
    }
    return swaps
}

minimumSwaps(a)
