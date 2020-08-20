function run(section) {
  console.log(`ran through ${section}`)
}

function rest() {
  console.log('resting...')
}

const sections = ["LA", "NY", "MI"]
// for loop
for (let i = 0; i<sections.length; i++) {
  run(sections[i])
  rest()
}
console.log('------------------------');
// while loop
let j = 0
while (j < sections.length) {
  run(sections[j])
  rest()
  j++
}

