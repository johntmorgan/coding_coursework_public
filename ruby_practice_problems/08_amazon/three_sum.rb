require 'set'
def three_sum(numbers)
  res = []
  numbers.sort!
  (0...numbers.length()).each do |i|
    two_numbers(numbers, i, res)
  end
  return res
end

def two_numbers(numbers, i, res)
  seen = Set.new()
  j = i + 1
  (j...numbers.length()).each do |ji|
    complement = 0 - (numbers[i] + numbers[ji])
    if seen.include? complement
      res.push([numbers[i], numbers[ji], complement])
    end
    seen.add(numbers[ji])
  end
end

numbers = [3, 0, 6, 2, 5, -8, -1]
p(three_sum(numbers))