const Counter = function() {
  const counts = {}
  this.add = function(k, v=1) {
    if (!(k in counts)) {
      counts[k] = 0
    }
    counts[k] += v
  }
  this.getCount = function(k) {
    if (k in counts) {
      return counts[k]
    }
    return 0
  }
}

function countTriplets(arr, r) {
  let count = 0;
  const p2 = new Counter()
  const p3 = new Counter()

  arr.map(item => {
    count += p3.getCount(item)
    p3.add(item * r, p2.getCount(item))
    p2.add(item * r, 1)
  })

  console.log(count);
  
  return count;
}

countTriplets(
  [1, 1, 3, 3, 9],
  3
)
// export default countTriplets;
