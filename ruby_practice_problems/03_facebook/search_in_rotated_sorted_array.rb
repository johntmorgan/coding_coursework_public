def search_rotated(arr, key)
  left = 0
  right = arr.length() - 1
  while left <= right
    mid = ((left + right) / 2).to_i
    if arr[mid] == key
      return mid
    end

    if arr[left] < arr[mid]
      if key >= arr[left] && key < arr[mid]
        right = mid - 1
      else
        left = mid + 1
      end
    else
      if key > arr[mid] && key <= arr[right]
        left = mid + 1
      else
        right = mid - 1
      end
    end
  end
  return -1
end


arr = [4,5,6,7,0,1,2]
key = 2
p(search_rotated(arr, key))