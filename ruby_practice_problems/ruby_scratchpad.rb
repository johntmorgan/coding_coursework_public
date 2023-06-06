a = [0] * 8
p(a)

# copying array
b = a.map(&:itself)
b = a.map(&:clone)

a = [1, 2, 3]
p(a[0...2])
b = a.slice(0, a.length())
a[0] = 5
p(a)
p(b)

obj = {'one': 1, 'two': 2, 'three': 3}
obj.each do |item|
  p(item)
end

obj.keys().each do |key|
  p(key)
end

obj.values().each do |key|
  p(key)
end

p("Hello".slice(1, 3))

a = [1, 2, 3]
a.insert(0,4); # or [4] + a - creates new array
p(a)
a.shift()
p(a)

a = "vegancookbook"
p(a[0...5])