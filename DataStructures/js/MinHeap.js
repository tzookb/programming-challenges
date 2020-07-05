class MinHeap {
  constructor() {
    this.items = []
  }

  getParentIdx(i) {
    if (i == 0) {
      return null;
    }
    return Math.floor((i -1) / 2)
  }

  getLeftIdx(i) {
    return (2 * i) + 1
  }

  getRightIdx(i) {
    return (2 * i) + 2
  }

  //It returns the root element of Min Heap. Time Complexity of this operation is O(1).
  getMin() {
    return this.items[0]
  }

  //Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
  extractMin() {
    const last = this.items.pop()
    if (this.items.length == 0) {
      return last
    }
    const first = this.items[0]
    this.items[0] = last

    let curI = 0
    while (true) {
      const leftI = this.getLeftIdx(curI)
      const rightI = this.getRightIdx(curI)
      const leftV = this.items[leftI]
      const rightV = this.items[rightI]
      const curV = this.items[curI]
      
      if (leftV !== undefined && rightV !== undefined) {        
        if (leftV < rightV && leftV < curV) {
          this._swap(leftI, curI) 
          curI = leftI
        } else if (leftV >= rightV && rightV < curV) {
          this._swap(rightI, curI) 
          curI = rightI
        } else {
          break
        }
      } else if (leftV != undefined) {
        if (leftV < curV) {
          this._swap(leftI, curI) 
          curI = leftI
        } else {
          break
        }
      } else if (rightV != undefined) {
        if (rightV < curV) {
          this._swap(rightI, curI) 
          curI = rightI
        } else {
          break
        }
      } else {
        break;
      }
    }

    return first
  }

  //Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
  insert(val) {
    this.items.push(val)
    let index = this.items.length - 1
    //bubble up
    
    while (index > 0) {
      let parentIdx = this.getParentIdx(index)
      if (this.items[parentIdx] <= this.items[index]) {
        break
      }
      const temp = this.items[parentIdx]
      this.items[parentIdx] = this.items[index]
      this.items[index] = temp
      index = parentIdx
    }
  }

  _swap(fpos,spos) 
  { 
      let tmp = this.items[fpos]
      this.items[fpos] = this.items[spos]; 
      this.items[spos] = tmp; 
  } 
}

module.exports = MinHeap

let m = new MinHeap()
m.insert(0)
m.insert(2)
m.insert(5)
const list = []
console.log(m.items)
console.log(m.extractMin());
console.log(m.extractMin());
console.log(m.extractMin());


