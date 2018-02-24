function miniMaxSum(arr) {
    arr.sort();
    console.log(arr.slice(0,-1).reduce((v,s)=>v+s, 0) + " " + arr.slice(1).reduce((v,s)=>v+s, 0));
}