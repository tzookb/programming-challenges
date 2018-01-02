function buyMaximumProducts(n, k, a) {
    let willSortArr = [].concat(a);
    let sortedIndexes = sortWithIndeces(willSortArr);
    
    let cash = k+0;
    let totalStocks = 0;

    
    for (let i=0; i<sortedIndexes.length; i++) {
        const price = a[sortedIndexes[i]];
        let canBuyNow = Math.floor(cash/price);
        
        if (canBuyNow === 0) {
            return totalStocks;
        }

        canBuyNow = Math.min(canBuyNow, sortedIndexes[i]+1)

        console.log('price: '+price+' canBuy: '+canBuyNow+' cash: '+cash);
        
        totalStocks += canBuyNow;
        cash -= canBuyNow*price;
    }
    return totalStocks;
}

let n = 3;
let a = [10, 7, 19];
let k = 45;

let res = buyMaximumProducts(n,k,a);
console.log(res);



function sortWithIndeces(toSort) {
  for (var i = 0; i < toSort.length; i++) {
    toSort[i] = [toSort[i], i];
  }
  toSort.sort(function(left, right) {
    return left[0] < right[0] ? -1 : 1;
  });
  toSort.sortIndices = [];
  for (var j = 0; j < toSort.length; j++) {
    toSort.sortIndices.push(toSort[j][1]);
    toSort[j] = toSort[j][0];
  }
  return toSort.sortIndices;
}
