require './heap2.rb'

# O(nlogk) time
# O(n) space

def median_sliding_window(nums, k)
  medians = []
  hmap = Hash.new
  small_list = MaxHeap.new
  large_list = MinHeap.new

  (0...k).each do |i|
    small_list.push(nums[i])
  end

  (0...k/2).each do |j|
    large_list.push(small_list.pop())
  end

  i = k
  while true
    if k % 2 == 0
      medians.push((small_list.max()) + (large_list.min()) * 0.5)
    else
      medians.push((small_list.max()).to_f)
    end

    if i >= nums.length()
      break
    end

    out_num = nums[i - k]
    in_num = nums[i]
    i += 1
    balance = 0

    if hmap[out_num] != nil
      hmap[out_num] += 1
    else
      hmap[out_num] = 1
    end

    if out_num <= small_list.max()
      balance -= 1
    else
      balance += 1
    end

    if !small_list.empty? and in_num <= small_list.max()
      small_list.push(in_num)
      balance += 1
    else
      large_list.push(in_num)
      balance -= 1
    end

    # Shift lists depending on balance in/out

    if balance < 0
      small_list.push(large_list.pop())
    end

    if balance > 0
      large_list.push(small_list.pop())
    end

    # Remove any old numbers from top of both heaps if you can

    num = hmap[small_list.max()].to_i
    while !small_list.empty? && num > 0
      hmap[small_list.max()] -= 1
      small_list.pop()
      num = hmap[small_list.max()].to_i
    end

    num = hmap[large_list.min()].to_i
    while !large_list.empty? && num > 0
      hmap[large_list.min()] -= 1
      large_list.pop()
      num = hmap[large_list.min()].to_i
    end
  end
  return medians
end

# Driver Code

puts("Example - 1")
arr = [1,3,-1,-3,5,3,6,7]
k = 3
print ("Input: array = " + arr.to_s + ", k = " + k.to_s)
puts()
output = median_sliding_window(arr,k).map(&:to_i)
print("Output: Medians =",output)
puts()


puts("Example - 2")
arr = [1,2]
k = 1
print ("Input: array = " + arr.to_s + ", k = " + k.to_s)
puts()
output = median_sliding_window(arr,k).map(&:to_i)
print("Output: Medians =",output)
puts()