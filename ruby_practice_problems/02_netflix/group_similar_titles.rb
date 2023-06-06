# Want to group anagrams together
# Compute 26 element vector
# Use vector to insert in hash map

# Time O(n * k) n number of strings, k max length of string
# Space complexity O(n * k) n number of strings, size of strings can be k
  # Isn't it O(n * 26) -> O(n)? - JM

def group_titles(strs)
  res = {}
  strs.each do |str|
    count = [0] * 26
    str.each_char do |c|
      ci = c.ord - 'a'.ord
      count[ci] += 1
    end

    key = count.to_s
    if res.include? key
      res[key].push(str)
    else
      res[key] = [str]
    end
  end
  return res.values()
end

# Driver code

titles = ["duel","dule","speed","spede","deul","cars"]
gt = group_titles(titles)
query = "spede"

# Searching for all titles
gt.each do |g|
  if g.include? query
    p(g)
  end
end