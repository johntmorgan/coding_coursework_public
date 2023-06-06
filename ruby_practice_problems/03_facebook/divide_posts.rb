# Review

# O(nlogm time - binary search takes Olog(m), each mid pick results in n element traversal)
# O(1) space

def divide_posts(days, k)
  low, high = 1, days.sum() / k
  while low < high
    mid = (low + high + 1) / 2
    target = 0
    divisions = 0
    days.each do |posts|
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
  return high
end

# Driver code
days = [1000,2000,3000,4000,5000]
nodes = 3
puts ("The master node was assigned " + divide_posts(days, nodes).to_s + " posts")