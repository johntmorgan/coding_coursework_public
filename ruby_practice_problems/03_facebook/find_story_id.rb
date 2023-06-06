def find_story_id(arr, key)
  left = 0
  right = arr.length() - 1

  if left > right
    return
  end

  while left <= right
    mid = (left + right) / 2
    if arr[mid] == key
      return mid
    end

    if arr[left] <= arr[mid]
      if key <= arr[mid] && key >= arr[left]
        right = mid - 1
      else
        left = mid + 1
      end
    elsif arr[mid] <= arr[right]
      if key >= arr[mid] && key <= arr[right]
        left = mid + 1
      else
        right = mid - 1
      end
    else
      return -1
    end
  end
  return -1
end

v1 = [6, 7, 1, 2, 3, 4, 5]
puts("Story(3) found at index: " + (find_story_id(v1, 3)).to_s)
puts("Story(6) found at index: " + (find_story_id(v1, 6)).to_s)

v2 = [5,6,7,8,9,10,11,12,1,2,3,4]

puts("Story(3) found at index: " + (find_story_id(v2, 3)).to_s)
puts("Story(6) found at index: " + (find_story_id(v2, 6)).to_s)