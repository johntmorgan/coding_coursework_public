require './LinkedList2.rb'

# Linked list operations - note from course
# insert_at_tail(key, data)
# remove_node(node)
# remove_head()
# remove_tail()
# get_head()
# get_tail()

# O(1) for everything
# O(k) space - size of linked list

class LRUStructure

  attr_accessor :capacity, :size, :chash, :cache
  def initialize(capacity)
    @capacity = capacity
    @chash = {}
    @cache = LinkedList.new()
  end

  def set(key, value)
    if !@chash.include? key
      if @cache.size < @capacity
        @cache.insert_at_tail(key, value)
        @chash[key] = @cache.tail
      else
        @cache.remove_head
        @cache.insert_at_tail(key, value)
        @chash[key] = @cache.tail
      end
    else
      node = @chash.key
      @cache.remove_node(node)
      @cache.insert_at_tail(key, value)
      @chash[key] = @cache.tail
    end
  end

  def get(key)
    if !@chash.include? key
      return nil
    else
      value = @chash[key].data
      @cache.remove_node(@chash[key])
      @cache.insert_at_tail(key, value)
      return @cache
    end
  end

  def print_data()
    node = @cache.get_head()
    while node != nil
      print("(" + (node.key).to_s + "," + (node.data).to_s + ")")
      STDOUT.flush
      node = node.next
    end
    puts("\n")
  end
end



# Driver code
puts("The most recent wathced titles are: (key, value)")
obj = LRUStructure.new(3)
obj.set(10, 20)
obj.print_data()

obj.set(15, 25)
obj.print_data()

obj.set(20, 30)
obj.print_data()

obj.set(25, 35)
obj.print_data()

obj.set(5, 40)
obj.print_data()

obj.get(25)
obj.print_data()