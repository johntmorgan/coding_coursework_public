
# O(n) space
# O(n) time
# Why not just iterate push_forward and pop backwards, save space? - JM

# def verify_session(push_op, pop_op)
#   stack = []
#   push_op.each do |push_item|
#     i = 0
#     stack.push(push_item)
#     while stack.length() > 0 && stack[-1] == pop_op[i]
#       stack.pop()
#       i += 1
#     end
#   end
#   return stack.empty?
# end

def verify_session(push_op, pop_op)
  i = pop_op.length() - 1
  push_op.each do |push_item|
    if push_item != pop_op[i]
      return false
    end
    i -= 1
  end
  return true
end

push_op = [1,2,3,4,5]
pop_op = [5,4,3,2,1]

if verify_session(push_op, pop_op)
    puts("Session Successful!")
else
    puts("Session Faulty!")
end

push_op = [1,2,3,4,5]
pop_op = [4,5,3,2,1]

if verify_session(push_op, pop_op)
    puts("Session Successful!")
else
    puts("Session Faulty!")
end