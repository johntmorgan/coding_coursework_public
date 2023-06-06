def max_profit(arr)
  return 0 if arr.length() < 1
  curr_max = arr[0]
  global_max = arr[0]
  arr.each do |val|
    if curr_max < 0
      curr_max = val
    else
      curr_max += val
    end

    if global_max < curr_max
      global_max = curr_max
    end
  end
  return global_max
end

stocks = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
puts("Maximum Profit: " + (max_profit(stocks)).to_s + '%')