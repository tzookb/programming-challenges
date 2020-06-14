const loadsh = require('lodash')

const isValidHttpUrl = item => true

const iterateObj = obj => {
  for (let key in obj) {
    iterate(obj, key)
  }
  console.log(obj);
}
const iterate = (obj, path) => {
  let item = loadsh.get(obj, path)

  if (typeof item == "string" && isValidHttpUrl(item)) {
    loadsh.set(obj, path, 'updated...')
  }
  else if (typeof item == "array") {
    item.map((idx ,_) => iterateObj(obj, `${path}.${idx}`))
  }
  else if (typeof item == "object") {
    for (let key in item) {
      iterate(obj, `${path}.${key}`)
    }
  }
}

iterateObj({
  // x: 11,
  // z: {
  //   a: 11,
  //   b: 'xx'
  // },
  b: [
    1,2,'xx', {a:1, b:'ccc'}
  ]
})