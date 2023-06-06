def maximize_sweetness(sweetness, k)
  k += 1
  sum = 0
  sweetness.each do |sweet|
    sum += sweet
  end
  low, high = 1, sum / k
  while low < high
    mid = (low + high + 1) / 2
    target = 0
    divisions = 0
    sweetness.each do |posts|
      target += posts
      if target >= mid
        divisions += 1
        target = 0
      end
    end
    if divisions >= k
      low = mid
    else
      high = mid - 1
    end
  end
  return low
end

# Driver code
sweetness = [1, 2, 3, 4, 5]
k = 3
p(maximize_sweetness(sweetness, k))