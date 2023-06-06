# Assuming a SORTED array (doesn't work unsorted)
# Rather than going through each item sequentially (linear time)
# You start in the middle and cut in half each time (log time - log base 2 time)

def binary_search(list, item)
  low = 0
  high = list.length() - 1

  while low <= high
    mid = (low + high) / 2
    guess = list[mid]

    if guess == item
      return mid
    elsif guess < item
      low = mid + 1
    else guess > item
      high = mid - 1
    end
  end
end

puts binary_search([*1..100], 47)

# log2(n) steps
# Math.log(128, 2) = 7
# Specify base with second param as default is base e

