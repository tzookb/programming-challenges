function processData(input) {
	input = input.split('\n')[1].split(' ');
	return input.reduce(function(prev, curr) {
		curr = parseInt(curr);
		return prev ^ curr;
	}, 0);
}