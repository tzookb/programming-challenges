class ShoeResult {
	constructor(id) {
		this.id = id;
		this.deals = 0;
	}

	addDeal() {
		this.deals++;
	}
}

function getLatestSuggestion(numOfSuggestionToReturn, numberOfUniqueShoes, numOfOrders, deals) {
	let products = [];
	let i;
	for(i=0;i<numberOfUniqueShoes;i++) {
		products[i] = new ShoeResult(i);
	}
	deals.forEach(function(deal) {
		products[deal].addDeal();
	});


	products.sort(function(a, b){
		if (a.deals != b.deals) {
			return a.deals < b.deals;
		}
		return a.id > b.id;
	});

	console.log(products);
	
	let itemIds = products.map(function(item) {
		return item.id;
	});

	return itemIds.slice(0, numOfSuggestionToReturn);
}

function processData(data) {
	data = data.split('\n');

	let numOfSuggestionToReturn, numberOfUniqueShoes, numOfOrders;

	[numOfSuggestionToReturn, numberOfUniqueShoes, numOfOrders] = data[0].split(' ');
	data.shift();
	data = data.map(Number);
	let results = getLatestSuggestion(numOfSuggestionToReturn, numberOfUniqueShoes, numOfOrders, data);

	results.forEach(function(item) {
		console.log(item);
	});
}

let data = `
3 4 5
2
2
2
2
2
`.trim();
processData(data);