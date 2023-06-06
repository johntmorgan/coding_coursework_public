def max_profit(arr)
  curr = 1
  best_buy = arr[0]
  max_p = 0
  while curr < arr.length()
    best_buy = arr[curr - 1] if arr[curr - 1] < best_buy
    max_p = arr[curr] - best_buy if (arr[curr] - best_buy) > max_p
    curr += 1
  end
  return max_p
end

arr = [7,1,5,3,6,4]
p(max_profit(arr))

arr = [7, 6, 4, 3, 1]
p(max_profit(arr))