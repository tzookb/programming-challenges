var mergeKLists = function(lists) {
  const m = new MinHeap()
  lists.map(list => {
      let cur = list
      while (cur) {
          m.insert(cur.val)
          cur = cur.next
      }
  })

  const fake = new ListNode('dontcare', null)
  let resultList = fake
  let v
  
  while (true) {
      v = m.extractMin()
      if (v == null) {
          break
      }
      const temp = new ListNode(v, null)
      resultList.next = temp
      resultList = resultList.next
  }
  return fake.next
};