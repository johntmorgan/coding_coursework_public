def two_sum(numbers, target)
  hmap = {}
  numbers.each_with_index do |num, i|
    if hmap[num] != nil
      return [hmap[num], i]
    else
      hmap[target - num] = i
    end
  end
end


numbers = [83, 97, 25]
target = 108
p(two_sum(numbers, target))