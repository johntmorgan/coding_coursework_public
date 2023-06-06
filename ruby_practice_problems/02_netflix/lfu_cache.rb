require './LinkedList6.rb'

class LFUCache

  attr_accessor :cache, :capacity, :cache_vals
  def initialize(capacity)
    @capacity = capacity
    @freq_dict = {}
    @key_dict = {}
    @size = 0
    @min_freq = 0
  end

  def set(key, value)
    if @key_dict[key] == nil
      if @size == @capacity
        @freq_dict[@min_freq].delete(@freq_dict[@min_freq].head)
        @size -= 1
      end
      new_node = LinkedListNode.new(key, value, 1)
      @key_dict[key] = new_node
      @min_freq = 1
      if @freq_dict[@min_freq] == nil
        @freq_dict[@min_freq] = LinkedList.new()
        @freq_dict[@min_freq].append(new_node)
      else
        @freq_dict[@min_freq].append(new_node)
      end
      @size += 1
    else
      node = @key_dict[key]
      @freq_dict[node.freq].delete(node)
      node.val = value
      node.freq += 1
      if @freq_dict[node.freq] != nil
        @freq_dict[node.freq].append(node)
      else
        @freq_dict[node.freq] = LinkedList.new()
        @freq_dict[node.freq].append(new_node)
      end
      @min_freq += 1 if @freq_dict[@min_freq] == nil
    end
  end

  def get(key)
    if @key_dict[key] == nil
      return nil
    else
      node = @key_dict[key]
      @freq_dict[node.freq].delete(node)
      node.freq += 1
      if @freq_dict[node.freq] != nil
        @freq_dict[node.freq].append(node)
      else
        @freq_dict[node.freq] = LinkedList.new()
        @freq_dict[node.freq].append(new_node)
      end
      @min_freq += 1 if @freq_dict[@min_freq] == nil
      return node.val
    end
  end

  def get_cache()
    res = ""
    added = 0
    curr_freq = 1
    while added < @size
      node = @freq_dict[curr_freq].head
      while node
        res += "(" + (node.key).to_s + "," + (node.val).to_s +  ")"
        node = node.next
        added += 1
      end
      curr_freq += 1
    end
    return res
  end
end