require './LinkedList.rb'

# Linked list operations
# insert_at_tail(key, data)
# remove_node(node)
# remove_head()
# remove_tail()
# get_head()
# get_tail()

class LRUCache

  attr_accessor :cache, :capacity, :cache_vals
  def initialize(capacity)
    @capacity = capacity
    @cache = {}
    @cache_vals = LinkedList.new()
  end

  def set(key, value)
    if @cache[key] != nil
      @cache_vals.remove_node(@cache[key])
      @cache_vals.insert_at_tail(key, value)
      @cache[key] = @cache_vals.get_tail()
    else
      @cache_vals.remove_head() if @cache_vals.size() == capacity
      @cache_vals.insert_at_tail(key, value)
      @cache[key] = @cache_vals.get_tail()
    end
    return
  end

  def get(key)
    if @cache[key] == nil
      return nil
    else
      node = @cache[key]
      value = node.val
      @cache_vals.remove_node(node)
      @cache_vals.insert_at_tail(key, value)
      @cache[key] = @cache_vals.get_tail()
      return value
    end
  end

  def get_cache()
    res = ""
    node = @cache_vals.head
    while node
      res += "(" + (node.key).to_s + "," + (node.val).to_s +  ")"
      node = node.next
    end
    return res
  end
end