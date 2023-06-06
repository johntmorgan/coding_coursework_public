# Copied from stack overflow to experiment with

def factorial(num)
  n = num
  if n == 0
    1
  else 
    n * factorial(num - 1)
  end
end

puts factorial(10)