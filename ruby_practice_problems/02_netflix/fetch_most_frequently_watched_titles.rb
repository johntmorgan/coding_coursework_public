require './LinkedList3.rb'

class LFUStructure

  attr_accessor :freq_dict, :key_dict, :min_freq, :size, :capacity
  def initialize(capacity)
    @capacity = capacity
    @size = 0
    @min_freq = 0
    @freq_dict = {}
    @key_dict = {}
  end

  def get(key)
    if !key_dict.include? key
      return nil
    end

    node = @key_dict[key]
    @freq_dict[node.freq].delete(node)
    if (@freq_dict[@key_dict[key].freq].head) == nil
      @freq_dict.delete(@key_dict[key].freq)
      if (@min_freq == @key_dict[key].freq)
          @min_freq += 1
      end
    end

    node.freq += 1
    @key_dict[key] = node
    if (@freq_dict[node.freq] == nil)
      @freq_dict[node.freq] = LinkedList.new()
      @freq_dict[node.freq].append(node)
    else
      @freq_dict[node.freq].append(node)
    end

    return node.val
  end

  def set(key, value)
    if (get(key) != nil)
      @key_dict[key].val = value
      return
    end

    if @size == @capacity
      @key_dict.delete(@freq_dict[min_freq].head.key)
      if @freq_dict[@min_freq] == nil
        @freq_dict[@min_freq] = LinkedList.new()
      else
        @freq_dict[@min_freq].delete(@freq_dict[@min_freq].head)
      end
      if @freq_dict[@min_freq].head == nil
        @freq_dict.delete(@min_freq)
      end
      @size -= 1
    end

    @min_freq = 1
    node = LinkedListNode.new(key, value, @min_freq)
    @key_dict[key] = node
    if (@freq_dict[1] == nil)
      @freq_dict[1] = LinkedList.new()
      @freq_dict[1].append(node)
    else
      @freq_dict[1].append(node)
    end
  end

   def print_dict()
      @key_dict.each do |k,v|
         print("(" + k.to_s + ", " + v.val.to_s + ")")
         STDOUT.flush
      end

      puts("")
   end
end


puts("The most frequently watched titles are: (key, value)")
obj = LFUStructure.new(2)
obj.set(10, 20)
obj.set(15, 25)
obj.get(10);
obj.print_dict()
obj.set(20, 30)
obj.get(15);
obj.print_dict()
obj.set(25, 35)
obj.get(10)
obj.get(20)
obj.get(25)
obj.print_dict()