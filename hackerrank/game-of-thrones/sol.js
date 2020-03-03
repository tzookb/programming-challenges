function isKey(str) {
	let counts = {};
	let numOfOdds = 0;

	str.split('').forEach(function(item) {
		if (!(item in counts)) {
			counts[item] = 0;
		}
		counts[item]++;
	});

	for (let k in counts) {
		if (counts[k]%2 == 1) {
			numOfOdds++;
		}
	}
	// console.log(numOfOdds);
	// console.log(counts);
	return numOfOdds <= 1;
}

console.log(isKey('abbabba'));
console.log(isKey('abbaabba'));
console.log(isKey('abbasabba'));
console.log(isKey('ab'));
console.log(isKey('abb'));