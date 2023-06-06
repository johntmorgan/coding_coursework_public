def recur_permute(res, nums, curr)
  if curr == nums.length() && !res.include?(nums)
    app_arr = []
    nums.each do |elem|
      app_arr.push(elem)
    end
    res.push(app_arr)
    return
  else
    (curr...nums.length()).each do |pos|
      nums[curr], nums[pos] = nums[pos], nums[curr]
      recur_permute(res, nums, curr + 1)
      nums[pos], nums[curr] = nums[curr], nums[pos]
    end
  end
end

def permute(nums)
  res = []
  if nums.length() > 0
    nums_arr = nums[1...nums.length() - 1].split(",").map(&:to_i)
    recur_permute(res, nums_arr, 0)
  end
  return res
end

# nums = [1, 2, 3]
# p(permute(nums))

# p(permute([3,0,1,4]))
# p(permute([1,4,6,3]))
# p(permute([1]))
# p(permute([4,8]))

p(permute("[1,2,3]"))