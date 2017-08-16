function solve(numHurdles, initialJump, hurdles) {
     const diff = initialJump - Math.max.apply(null, hurdles);
     
     if (diff >= 0)
        return 0;
     return Math.abs(diff);
}

let res = solve(5, 7, [2, 5, 4, 9, 2]);
console.log(res);
