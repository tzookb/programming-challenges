// https://www.hackerrank.com/challenges/ctci-ransom-note

function arrayValsToObjectKeys(arr) {
	const newObj = {};

	arr.map(val => {
		if (val in newObj) {
			newObj[val] = newObj[val] + 1;	
		} else {
			newObj[val] = 1;
		}
	});

	return newObj;
}

function solve(magazine, ransome) {
	const magazineDict = arrayValsToObjectKeys(magazine);
	const ransomeDict = arrayValsToObjectKeys(ransome);
    
    for (let key in ransomeDict) {

    	if (key in magazineDict && magazineDict[key] >= ransomeDict[key]) {
    		//all good
    	} else {
    		return false;
    	}
    }
    return true;
}

const magazine = ["wi", "z", "ne", "we", "ebixk", "yvrd", "qrd", "ojckw", "q", "xe", "e", "bcco", "xb", "ieqym", "dwuu", "w", "dnapw", "achkt", "xqdhs", "nstms", "zmqu", "csqxi", "rim", "tvic", "arq", "fvjqx", "x", "su", "ty", "zl", "zmah", "y", "tv", "rkjq", "hpvpx", "ujj", "f", "i", "u", "fl", "iv", "n", "mnrvx", "tho", "diz", "k", "tidi", "gr", "ptkq", "z", "tho", "su", "diz", "yvrd", "dwuu", "dnapw", "xb", "arq", "xb", "mnrvx", "xe", "bcco", "qrd", "y", "ptkq", "rim", "fvjqx", "bcco", "q", "q", "wi", "i", "tidi", "gr", "mnrvx", "hpvpx", "tv", "f", "y", "mnrvx", "we", "fvjqx", "tv", "f", "wi", "ptkq", "ujj", "rim", "ebixk", "tho", "ptkq", "rkjq", "yvrd", "dwuu", "zl", "ujj", "zl", "qrd", "e", "ieqym"];

const ransome = ["dwuu", "tvic", "y", "dnapw", "ujj", "tidi", "nstms", "x", "xe", "achkt", "x", "su", "zmqu", "iv", "zmqu", "xb", "ojckw", "we", "fvjqx", "tvic", "tv", "ne", "rkjq", "diz", "tvic", "we", "rkjq", "nstms", "zmah", "ieqym", "zmah", "fl", "xb", "wi", "tho", "x", "z", "ty", "u", "i", "gr", "ptkq", "q", "su", "tho", "rim", "tv", "iv", "iv", "yvrd", "xe", "qrd", "y", "dnapw", "q", "zmah", "arq", "we", "ieqym", "su", "zl", "q", "xb", "arq", "rkjq", "q", "e", "xb", "zl", "ty", "fvjqx", "ptkq", "ieqym", "qrd", "y", "wi", "wi", "nstms", "diz", "dnapw", "zmah", "q", "ebixk", "su", "e", "xb", "q", "i", "mnrvx", "wi", "x", "x", "tidi", "w", "ojckw", "bcco", "e", "tv", "rkjq", "tho"];



const result = solve(magazine, ransome);
console.log(result);
