require './Stack.rb'

class MaxStack

  attr_accessor :main_stack, :max_stack
  def initialize()
    @main_stack = MyStack.new()
    @max_stack = MyStack.new()
    return
  end

  def pop()
    @max_stack.pop()
    return @main_stack.pop()
  end

  def push(value)
    @main_stack.push(value)
    if max_stack.size() == 0 || value > @max_stack.top()
      @max_stack.push(value)
    else
      @max_stack.push(@max_stack.top())
    end
  end

  def max_rating()
    return @max_stack.top()
  end
end

ratings = MaxStack.new()
ratings.push(5)
ratings.push(0)
ratings.push(2)
ratings.push(4)
ratings.push(6)
ratings.push(3)
ratings.push(10)

p(ratings.main_stack.stack_list)
puts("Maximum Rating: " + String(ratings.max_rating()))

ratings.pop() # Back button effect
puts("\nAfter clicking back button\n")
p(ratings.main_stack.stack_list)
puts("Maximum value: " + String(ratings.max_rating()))