# Time O(n) - is really O(n * log(c)) but log(c) is a constant
# Space O(1) - O(c) -> O(1)

require './heap.rb'

def reorganize_results(initial_order)
  # count = initial_order.split("").inject(Hash.new(0)) { |m, n| m[n] += 1; m }
  count = {}
  initial_order.each_char do |c|
    if count[c] == nil
      count[c] = 1
    else
      count[c] += 1
    end
  end
  max_freq = count.values().max()
  heap = Heap.new()
  count.each do |c, freq|
    heap.push([freq * -1, c])
  end

  result = []
  while heap.size > 0
    curr = heap.pop()
    freq = curr[0]
    char = curr[1]
    if result == nil or char != result[-1]
      result.push(char)
      heap.push([freq + 1, char]) if freq != -1
    else
      return initial_order if heap.size() == 0
      curr2 = heap.pop()
      freq2 = curr2[0]
      char2 = curr2[1]
      result.push(char2)
      heap.push([freq, char])
      heap.push([freq2 + 1, char2]) if freq2 != -1
    end
  end
  return result.join('')
end

initial_order = "bbnnc"
p(reorganize_results(initial_order))

initial_order = "bbbbnnc"
p(reorganize_results(initial_order))

initial_order = "bbbbbnnc"
p(reorganize_results(initial_order))