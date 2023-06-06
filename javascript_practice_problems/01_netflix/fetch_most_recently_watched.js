import {LinkedListNode, LinkedList} from './LinkedList.js'

class LRUCache {
  constructor(capacity) {
    this.capacity = capacity
    this.cache = {}
    this.cacheVals = new LinkedList()
  }

  Set(key, value) {
    if (this.cache[key] == null){
      this.evictIfNeeded();
      var newNode = new LinkedListNode(key, value);
      this.cacheVals.insertAtTail(newNode);
      this.cache[key] = newNode;
    }
    else {
      this.cacheVals.remove(this.cache[key]);
      var newNode = new LinkedListNode(key, value);
      this.cacheVals.insertAtTail(newNode);
      this.cache[key] = newNode;
    }
  }

  Get(key) {
    if(this.cache[key] == null){
      return null;
    }
    else {
      var value = this.cache[key].data;
      this.cacheVals.remove(this.cache[key]);
      var node = new LinkedListNode(key, value);
      this.cacheVals.insertAtTail(node);
      return node;
    }
  }

  evictIfNeeded() {
    if (this.cacheVals.size >= this.capacity) {
      node = this.cacheVals.removeHead()
      delete this.cache[node.key]
    }
  }

  printcache() {
    let node = this.cacheVals.head
    while (node) {
      process.stdout.write("(" + node.key + "," + node.data + ")")
      node = node.next
    }
    console.log()
  }
}