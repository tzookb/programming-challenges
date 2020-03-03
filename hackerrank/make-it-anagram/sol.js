function getSumOfCountsFromCounter(cnt) {
	let counter = 0;

	for (let char in cnt) {
		counter += cnt[char];
	}
	return counter;
}

function getDiffOfCharCounts(c1, c2) {
	for (let charInC2 in c2) {
		if (charInC2 in c1) {
			if (c2[charInC2] == c1[charInC2]) {
				delete c1[charInC2];
			} else {
				c1[charInC2] = Math.abs(c2[charInC2]-c1[charInC2]);
			}
		} else {
			c1[charInC2] = c2[charInC2];
		}
	}
	return c1;
}

function getCharCountsInStr(str) {
	let counts = {};
	
	str.split('').forEach(function(char) {
		if ( ! (char in counts)) {
			counts[char] = 0;
		}
		counts[char]++;
	});
	return counts;
}

function getAnagramDiff(str1, str2) {
	let str1Counts = getCharCountsInStr(str1);
	let str2Counts = getCharCountsInStr(str2);

	let res = getDiffOfCharCounts(str1Counts, str2Counts);

	return getSumOfCountsFromCounter(res);
}


function processData(input) {
    console.log(getAnagramDiff(...input.split('\n')));
}