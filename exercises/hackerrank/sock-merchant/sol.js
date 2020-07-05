function sockMerchant(n, socks) {
  let countPairs = 0;
  const sockCounter = {};

  socks.map(sock => {
    if (!(sock in sockCounter)) {
      sockCounter[sock] = 0
    }
    sockCounter[sock]++
  })
  
  for (let sockColor in sockCounter) {
    const socksAmount = sockCounter[sockColor]
    const amountOfPairs = Math.floor(socksAmount/2)
    countPairs += amountOfPairs
  }
  return countPairs
}

console.log(
	getSocksPairs([10, 20, 20, 10, 10, 30, 50, 10, 20])
);
