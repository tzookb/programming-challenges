function getSocksPairs(socks) {
	var counters = {};
	var pairs = 0;

	for (var i=0 ; i<socks.length ; i++) {
		var cur = socks[i];

		if (cur in counters) {
			counters[cur]++;
		} else {
			counters[cur] = 1;
		}
	}

	for (var counterKey in counters) {
		pairs += Math.floor(counters[counterKey]/2);
	}
	return pairs;
}

console.log(
	getSocksPairs(
		"10 20 20 10 10 30 50 10 20".split(" ").map(sock => parseInt(sock))
	)
);