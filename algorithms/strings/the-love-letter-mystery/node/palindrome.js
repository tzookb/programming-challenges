let getCharCode = function(char) {
	return char.charCodeAt(0);
}
let removeMiddleChar = function(str) {
	if (str.length%2 == 1) {
		let index = parseInt(str.length/2);
		let character = '';
		str = str.substr(0, index) + character + str.substr(index+1);
	}
	return str;
};

let getPalindromeSteps = function(str) {
	str = removeMiddleChar(str);
	let steps = 0;
	let length = str.length;
	let middle = parseInt(length/2);
	
	for (let i=0; i<middle; i++) {
		if (str[i] != str[length-i-1]) {
			let left = getCharCode(str[i]);
			let right = getCharCode(str[length-i-1]);
			steps += Math.abs(left-right);
		}
	}

	return steps;
};


// this method is for hackerank tester not for the code resolution 
let processData = function(str) {
	let chunks = str.split('\n');
    for (let i=1; i<chunks.length; i++) {
        let steps = getPalindromeSteps(chunks[i]);
        console.log(steps);
    }    
};


module.exports = {removeMiddleChar, getCharCode, getPalindromeSteps};