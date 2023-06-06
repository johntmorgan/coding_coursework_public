def is_monotonic(arr)
  increasing, decreasing = true, true
  (0...arr.length() - 1).each do |i|
    if arr[i] < arr[i + 1]
      decreasing = false
    elsif arr[i] > arr[i + 1]
      increasing = false
    end
  end
  return increasing || decreasing
end