def smallest_sequence(list_a , list_b)
  if list_a.empty? || list_b.empty?
    return []
  end

  hash_list_b = {}
  list_b.each do |elem|
    if hash_list_b.include? elem
      hash_list_b[elem] += 1
    else
      hash_list_b[elem] = 1
    end
  end

  target_list = {}
  hash_list_b.keys().each do |key|
    target_list[key] = 0
  end

  min_dist = Float::INFINITY
  best = [nil, nil]
  left, right = 0, 0
  valid_chars = 0
  valid_target = hash_list_b.keys().length()
  while right < list_a.length()
    if valid_chars != valid_target
      while !target_list.include? list_a[right]
        right += 1
      end
      target_list[list_a[right]] += 1
      if target_list[list_a[right]] == hash_list_b[list_a[right]]
        valid_chars += 1
      end
      right += 1
    else
      while !target_list.include? list_a[left]
        left += 1
      end
      if right - left + 1 < min_dist
        min_dist = right - left + 1
        best = [left, right - 1]
      end
      target_list[list_a[left]] -= 1
      if target_list[list_a[left]] < hash_list_b[list_a[left]]
        valid_chars -= 1
      end
      left += 1
    end
  end
  return best
end

list_a = ["corona","petrol","corona","corona","climate","petrol","corona","petrol"]
list_b = ["corona","petrol","climate"]
p(smallest_sequence(list_a, list_b))