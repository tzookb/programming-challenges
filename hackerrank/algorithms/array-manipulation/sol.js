let n = 5
let q = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]

function arrayManipulation(n, queries) {
    const arr = new Array(n).fill(0);
    queries.map(query => {
        const [start, end, val] = query
        arr[start-1] += val
        if (end === n) {
            return
        }
        arr[end] -= val
    })
    let max = arr[0]
    for (let i=1; i<n; i++) {
        arr[i] += arr[i-1] 
        if (arr[i] > max) {
            max = arr[i]
        }
    }
    return max
}

arrayManipulation(n, q)
