class Node {
  constructor(val) {
    this.data = val;
    this.next = null;
  }
}

class LinkedList {
  constructor(head = null) {
    this.head = head;
  }
}

const traversal = () => {
  let n = head;
  while (n !== null) {
    console.log(n.data);
    n = n.next;
  }
};

let head = new Node(1);
let second = new Node(2);
let third = new Node(3);

let list = new LinkedList(head);

head.next = second;
second.next = third;

traversal();
