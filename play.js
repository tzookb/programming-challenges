/**
 * Instructions:
 *
 * Code a recursive algorithm to answer the questions below. The "err" values should be ignored.
 *
 */



/**
 * Print the sum of all numbers in healthy object
 *
 * expected: 1031
 */


/**
 * print the sum of all apples, pears and peas
 *
 * expected: 317
 */


/**
 * print the array of carrots numbers
 *
 * expected: [2, 5, 8, 5, 3, 3, 2, 6, 222, 5]
 */

const healthy = {
    fruits: [
      [1, 5,
        [13, {
          apples: [1, 49, 31]
        }, 3]
      ], {
        pears: [98, 22, "err"]
      }
    ],
    vegetables: [
      50, {
        celery: [1, 4, 55]
      }, 3, [
        3, 4, 61, {
          carrots: [2, 5, {
            baby: [8, 5, 3]
          }, {
            chantenay: [3, 2]
          }, [6, 222], 5]
        }
      ]
    ],
    legumes: [
      3, 94, {
        lentils: [1, "err", 3, 49]
      }, [
        93, 7, [
          {
            peas: [2, 45, {
              sweet: [2, 4, 33, 29]
            }, 1]
          }
        ]
      ]
    ]
  }
  
  function sumForKeys(data: any, keys: string[]) {
    let total = 0;
  
    function sumRecuForKey(data: any, parents: string[]) {
      if (typeof(data) == 'number') {
        for (let pr of parents) {
          if (keys.indexOf(pr) != -1) {
            total += data;
          }
        }
      }
    
      if (Array.isArray(data)) {
        for (let item of data) {
          sumRecuForKey(item, parents);
        }
      } else if (typeof data === 'object') {
        for (let item in data) {
          sumRecuForKey(data[item], [...parents, item]);
        }
      }
    }
    sumRecuForKey(data, [])
  
    return total;
  }
  
  
  
  function sumRecu(data: any) {
    if (typeof(data) == 'number') {
      return data;
    }
    let total = 0;
  
    if (Array.isArray(data)) {
      for (let item of data) {
        total += sumRecu(item);
      }
    } else if (typeof data === 'object') {
      for (let item in data) {
        total += sumRecu(data[item]);
      }
    }
  
    return total;
  }
  
  console.log(
    sumForKeys(healthy, ['apples', 'pears', 'peas'])
  );