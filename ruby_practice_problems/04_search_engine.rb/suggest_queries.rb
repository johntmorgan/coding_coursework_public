# Time complexity O(n^2 + 2^n + l), n is query length l is length of dict
# Space O((n * 2^n) + l)

require 'set'
def break_query(query, dict)
  return helper(query, Set.new(dict), {})
end

def helper(query, dict, result)
  if !query
    return []
  end

  if result.include?(query)
    return result[query]
  end

  res = []
  dict.each do |word|
    if !query.start_with?(word)
      next
    elsif word.length() == query.length()
      res.push(word)
    else
      result_of_rest = helper(query[word.length()...query.length()], dict, result)
      result_of_rest.each do |item|
        item = word + " " + item
        res.push(item)
      end
    end
  end
  result[query] = res
  return res
end

query = "vegancookbook"
dict = ["an", "book", "car", "cat", "cook", "cookbook", "crash", "cream", "high", "highway", "i", "ice", "icecream", "low", "scream", "veg", "vegan", "way"]
p(break_query(query, dict))
query = "highwaycarcrash"
p(break_query(query, dict))