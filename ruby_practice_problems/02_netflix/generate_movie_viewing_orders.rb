
# Time O(n!)
# Space O(n) - max stack depth is n

def recur_permute(movies, res, curr, size)
  if curr.length() == size
    res.push(curr.map(&:itself))
    return
  end

  (0...movies.length()).each do |i|
    curr.append(movies[i])
    recur_permute(movies[0...i] + movies[i + 1...movies.length()], res, curr, size)
    curr.pop()
  end
end

def generate_permutations(movies)
  res = []
  size = movies.length()
  recur_permute(movies, res, [], size)
  return res
end

# Example #1
input = ["Frozen","Dune","Coco"]
output = generate_permutations(input)
print("Output 1: [")
print(output)
puts()

# Example #2
input = ["Frozen","Dune","Coco","Melificient"]
output = generate_permutations(input)
print("Output 2: [")
print(output)
puts()

# Example #3
input = ["Dune","Coco"]
output = generate_permutations(input)
print("Output 3: [")
print(output)
puts()

