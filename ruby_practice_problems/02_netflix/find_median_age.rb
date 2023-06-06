# Fetch relevant content based on age of users for specific country or region
# Need to update median age in real time
# Output median after input
# Store smaller half in one list, larger half in othe rlist

require './heap.rb'

# Insert age O(logn)
# Find median O(1)
# Space O(n) - storing all variables at once

class MedianOfAges
  def initialize
    @max_heap = MaxHeap.new()
    @min_heap = MinHeap.new()
  end

  def insert_age(num)
    if @max_heap.empty? || @max_heap.max >= num
      @max_heap.push(num)
    else
      @min_heap.push(num)
    end

    if @max_heap.size() > @min_heap.size() + 1
      max = @max_heap.max!
      @min_heap.push(max)
    elsif @max_heap.size() < @min_heap.size()
      min = @min_heap.min!
      @max_heap.push(min)
    end
  end

  def find_median
    if @max_heap.size() > @min_heap.size()
      return @max_heap.max()
    else
      return (@max_heap.max() + @min_heap.min()) / 2.0
    end
  end
end

medianAge = MedianOfAges.new()
medianAge.insert_age(22)
medianAge.insert_age(35)
puts("The recommended content will be for ages under: " + String(medianAge.find_median()))
medianAge.insert_age(30)
puts("The recommended content will be for ages under: " + String(medianAge.find_median()))
medianAge.insert_age(25)
puts("The recommended content will be for ages under: " + String(medianAge.find_median()))