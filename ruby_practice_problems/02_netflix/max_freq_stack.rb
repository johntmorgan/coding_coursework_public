class FreqStack
  def initialize
    @freq_stack = {}
    @elem_freq = {}
    @max_freq = 0
  end

  def push(data)
    if @elem_freq.include? data
      @elem_freq[data] += 1
    else
      @elem_freq[data] = 1
    end
    curr_freq = @elem_freq[data]
    if curr_freq > @max_freq
      @max_freq = curr_freq
    end
    if @freq_stack.include? curr_freq
      @freq_stack[curr_freq].push(data)
    else
      @freq_stack[curr_freq] = [data]
    end
  end

  def pop()
    result = nil
    if @freq_stack[@max_freq] != nil
      result = @freq_stack[@max_freq].pop()
      @elem_freq[result] -= 1
      while @max_freq > 0 && @freq_stack[@max_freq] == []
        @max_freq -= 1
      end
    end
    return result
  end
end