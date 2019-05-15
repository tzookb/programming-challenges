function pickingNumbers(a) {
    var counts = new Array(100);
    counts.fill(0);

    a.forEach(function (item) {
        counts[item]++;
    })

    var max = 0;
    for(var i = 1; i < counts.length; i++){
        if(counts[i] + counts[i - 1] > max){
            max = counts[i] + counts[i - 1];
        }
    }
    
    return max;
    
}

let a = [4, 6, 5, 3, 3, 1];

let res = pickingNumbers(a);

console.log(res);
