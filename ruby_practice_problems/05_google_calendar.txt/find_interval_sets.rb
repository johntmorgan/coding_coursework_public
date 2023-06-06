require './heap.rb'

def find_sets(intervals)
    count = 0
    heap = MinHeap.new()
    last_heap = MinHeap.new()
    intervals.each do |int|
        heap.push(int)
    end
    while heap.size > 0
        new_int = heap.pop()
        last_heap.pop() if (!last_heap.empty? && last_heap.min <= new_int[0])
        last_heap.push(new_int[1])
        count = last_heap.size if last_heap.size > count
    end
    return count
end

intervals = [[1, 4], [2, 5], [4, 8], [5, 6], [5, 8], [6, 7]]
p(find_sets(intervals))