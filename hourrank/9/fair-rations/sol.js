function rash(arr) {
	let steps = 0;
	for (let i=0; i<arr.length; i++) {
		if (arr[i]%2 == 0)	 continue;
		
		if (i == arr.length-1){
			break;
		}
		arr[i]++;
		arr[i+1]++;
		
		i--;
		steps++;
	}

	for (i=0;i<arr.length;i++) {
		if (arr[i]%2==1)	return "NO";
	}
	return steps*2;
}

let arr = [2,3,4,5,6];
// arr = [1,2];

console.log(rash(arr));