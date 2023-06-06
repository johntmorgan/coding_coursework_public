require './heap.rb'

class MedianOfStream
  def initialize
    @small_heap = MaxHeap.new()
    @large_heap = MinHeap.new()
  end

  def insert_num(num)
    if @large_heap.size() == 0 && @small_heap.size() == 0
      @small_heap.push(num)
    elsif @small_heap.max() >= num
      @small_heap.push(num)
    else
      @large_heap.push(num)
    end

    while @large_heap.size() > @small_heap.size()
      @small_heap.push(@large_heap.pop())
    end

    while @small_heap.size() > @large_heap.size() + 1
      @large_heap.push(@small_heap.pop())
    end
  end

  def find_median()
    if @small_heap.size() == 0
      return nil
    elsif @small_heap.size() == @large_heap.size()
      return (@small_heap.max() + @large_heap.min()) / 2.0
    else
      return @small_heap.max()
    end
  end
end