import {MinHeap, MaxHeap} from './Heap.js'

class MedianOfAges{
  constructor(){
    maxHeap = new MaxHeap()
    minHeap = new MinHeap()
  }

  insertAge(num){
    if (maxHeap.isEmpty() || maxHeap.getMax() >= num){
      maxHeap.insert(num)
    }
    else
      minHeap.insert(num)

    if (maxHeap.getSize() > (minHeap.getSize() + 1)){
      var max = maxHeap.removeMax()
      minHeap.insert(max)
    }
    else if (maxHeap.getSize() < minHeap.getSize()) {
      var min = minHeap.removeMin()
      maxHeap.insert(min)
    }
  }

  findMedian(){
    if( maxHeap.getSize() == minHeap.getSize()){
      // we have even number of elements, take the average of middle two elements
      return maxHeap.getMax() / 2.0 + minHeap.getMin() / 2.0
    }
    // because max-heap will have one more element than the min-heap
    return maxHeap.getMax() / 1.0
  }
}

// Driver code

var medianAge = new MedianOfAges()
medianAge.insertAge(22)
medianAge.insertAge(35)
console.log("The recommended content will be for ages under: " + medianAge.findMedian())
medianAge.insertAge(30)
console.log("The recommended content will be for ages under: " + medianAge.findMedian())
medianAge.insertAge(25)
console.log("The recommended content will be for ages under: " + medianAge.findMedian())