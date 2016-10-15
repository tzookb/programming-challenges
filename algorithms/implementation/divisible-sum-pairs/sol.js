function getAmountOfPairs(n, k, nums) {
	var counter = 0;

	for (var i = 0; i<nums.length-1 ; i++) {
		for (var j=i+1 ; j<nums.length ; j++) {
			if ((nums[i]+nums[j])%k == 0) {
				counter++;
			}	
		}
	}
	return counter;
}

function getAmountOfPairsRecursive(k, nums) {
	var counter = 0;
	var elm = nums.shift();

	for (var i = 0; i<nums.length ; i++) {
		if ((elm+nums[i])%k == 0) {
			counter++;
		}	
	}
	if (nums.length==0) {
		return counter;
	} else {
		return counter + getAmountOfPairsRecursive(k, nums);
	}
}

console.log(getAmountOfPairsRecursive(3,[1,3,2,6,1,2]));