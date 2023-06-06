def validate_stack_sequences(pushed, popped)
  stack = []
  (0...pushed.length()).each do |i|
    stack.push(pushed[i])
    while stack.length() > 0 && popped.length() > 0 && popped[0] == stack[-1]
      popped.shift()
      stack.pop()
    end
  end
  return stack.empty?
end