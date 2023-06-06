# O(n^2) time - can traverse entire matrix
# O(n) space - visited array length

def dfs_friends(friends, n, visited, row)
  (0...n).each do |i|
    if friends[row][i] == 1 && visited[i] == 0 && row != i
      visited[i] = 1
      dfs_friends(friends, n, visited, i)
    end
  end
end

def friend_circles(friends, n)
  num_circles = 0
  if n == 0
    return num_circles
  else
    visited = Array.new(n, 0)
    (0...n).each do |i|
      if (visited[i] == 0)
        visited[i] += 1
        num_circles += 1
        dfs_friends(friends, n, visited, i)
      end
    end
  end
  return num_circles
end


n = 4
friends = Array([
  [1,1,0,0],
  [1,1,1,0],
  [0,1,1,0],
  [0,0,0,1]
])

puts ("Number of friend circles: " + (friend_circles(friends, n)).to_s)