export class MinHeap{
    constructor(){
        this.heap = []
        this.elements = 0
    }

    insert(val) {
        if (this.elements >= this.heap.length){
            this.elements = this.elements + 1
            this.heap.push(val)
            this.__percolateUp(this.heap.length - 1)
        }
        else{
            this.heap[this.elements] = val
            this.elements = this.elements + 1
            this.__percolateUp(this.elements - 1)
        }
    }

    getMin() {
        if (this.heap.length != 0)
            return this.heap[0]
        return null;
    }

    getSize() {
        return this.heap.length
    }

    removeMin() {
        if (this.elements > 1) {
            var min = this.heap[0]
            this.heap[0] = this.heap[this.elements - 1]
            this.elements = this.elements - 1
            this.heap.pop()
            this.__minHeapify(0)
            return min
        } else if (this.elements == 1) {
            var min = this.heap[0]
            this.elements = this.elements - 1
            heap = [];
            return min
        } else {
            return null;
        }
    
    }

    __percolateUp(index) {
        var parent = Math.floor( (index - 1) / 2)
        if (index <= 0)
            return
        else if (this.heap[parent] > this.heap[index]) {
            var tmp = this.heap[parent]
            this.heap[parent] = this.heap[index]
            this.heap[index] = tmp
            this.__percolateUp(parent)
        }
    }
    __minHeapify(index) {
        var left = (index * 2) + 1;
        var right = (index * 2) + 2;
        var smallest = index;
        if ((this.elements > left) && (this.heap[smallest] > this.heap[left])) {
            smallest = left
        }
        if ((this.elements > right) && (this.heap[smallest] > this.heap[right]))
            smallest = right
        if (smallest != index) {
            var tmp = this.heap[smallest]
            this.heap[smallest] = this.heap[index]
            this.heap[index] = tmp
            this.__minHeapify(smallest)
        }
    }

    buildHeap(arr){
        this.heap = arr
        this.elements = this.heap.length
        for (var i = this.heap.length - 1 ; i >= 0 ; i--){
            this.__minHeapify(i)
        }

    }

    isEmpty(){
        if (this.heap.length == 0) 
            return true
        else
            return false
    }

}

export class MaxHeap {
    constructor() {
        this.heap = []
        this.elements = 0
    }

    insert(val) {
        if (this.elements >= this.heap.length){
            this.elements = this.elements + 1
            this.heap.push(val)
            this.__percolateUp(this.heap.length - 1)
        }
        else{
            this.heap[this.elements] = val
            this.elements = this.elements + 1
            this.__percolateUp(this.elements - 1)
        }
    }

    getMax() {
        if (this.elements != 0)
            return this.heap[0]
        return null;
    }

    getSize() {
        return this.heap.length
    }

    removeMax() {
        if (this.elements > 1) {
            var max = this.heap[0]
            this.heap[0] = this.heap[this.elements - 1]
            this.elements = this.elements - 1
            this.heap.pop()
            this.__maxHeapify(0)
            return max
        } else if (this.elements == 1) {
            var max = this.heap[0]
            this.elements = this.elements - 1
            this.heap = []
            return max
        } else {
            return null
        }
    }

    __percolateUp(index) {
        var parent = Math.floor( (index - 1) / 2)
        if (index <= 0)
            return
        else if (this.heap[parent] < this.heap[index]) {
            var tmp = this.heap[parent]
            this.heap[parent] = this.heap[index]
            this.heap[index] = tmp
            this.__percolateUp(parent)
        }
    }
    __maxHeapify(index) {
        var left = (index * 2) + 1
        var right = (index * 2) + 2
        var largest = index;
        if ((this.elements > left) && (this.heap[largest] < this.heap[left])) {
            largest = left
        }
        if ((this.elements > right) && (this.heap[largest] < this.heap[right]))
            largest = right
        if (largest != index) {
            var tmp = this.heap[largest]
            this.heap[largest] = this.heap[index]
            this.heap[index] = tmp
            this.__maxHeapify(largest)
        }
    }

    buildHeap(arr){
        this.heap = arr
        this.elements = this.heap.length
        for (var i = this.heap.length - 1; i >= 0; i--){
            this.__maxHeapify(i)
        }
    }

    isEmpty(){
        if (this.heap.length == 0) 
            return true
        else
            return false
    }

}