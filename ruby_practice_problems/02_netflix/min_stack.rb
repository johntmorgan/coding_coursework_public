require './Stack.rb'

class MinStack

  attr_accessor :main_stack, :min_stack
  def initialize()
    @main_stack = MyStack.new()
    @min_stack = MyStack.new()
  end

  def push(value)
    @main_stack.push(value)
    top = @min_stack.top()
    if top != nil && top < value
      @min_stack.push(top)
    else
      @min_stack.push(value)
    end
  end

  def pop()
    @min_stack.pop()
    return @main_stack.pop()
  end

  def min()
    return @min_stack.top()
  end
end