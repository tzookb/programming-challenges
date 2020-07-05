
class Stack {

  constructor() {
    this.items = [];
  }

  push(val) {
    this.items.push(val);
  }
  
  pop(val) {
    return this.items.pop();
  }

  size() {
    return this.items.length;
  }

}


module.exports = Stack;