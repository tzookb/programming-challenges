function calcArbitrage(usdToEuro, euroToGbp, gbpToUsd) {
	let initialCash = 100000;
	let res = initialCash/usdToEuro;
	res = res/euroToGbp;
	res = res/gbpToUsd;
	if (res>initialCash)	return res - initialCash;

	return 0;
}

function processData(input) {
    input = input.split("\n");
    input.shift();
    input.forEach(function(testData) {
    	testData = testData.split(' ').map(Number);
    	console.log(calcArbitrage(testData[0], testData[1], testData[2]));
    });
} 

let input = `
2
1.1837 1.3829 0.6102
1.1234 1.2134 1.2311
`.trim();

processData(input);