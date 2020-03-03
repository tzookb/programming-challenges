function reverse(head) {
  let cur = head
  while (1) {
      const next = cur.next;
      const prev = cur.prev;
      cur.prev = next;
      cur.next = prev;
      if (!next) {
          break
      }
      cur = next;
  }
  return cur;
}