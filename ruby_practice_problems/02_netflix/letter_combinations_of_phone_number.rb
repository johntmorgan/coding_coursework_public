def lc_recur(digits, combinations, mapping, curr, index)
   if index == digits.length()
      combinations.push(curr)
      return
   end

   while digits[index] == "1" && index < digits.length()
      index += 1
      if index == digits.length()
         combinations.push(curr)
         return
      end
   end

   mapping[digits[index]].each do |digit|
      lc_recur(digits, combinations, mapping, curr + digit, index + 1)
   end
end

def letter_combinations(digits)
   combinations = []
   mapping = { "1" => [],
               "2" => ["a", "b", "c"],
               "3" => ["d", "e", "f"],
               "4" => ["g", "h", "i"],
               "5" => ["j", "k", "l"],
               "6" => ["m", "n", "o"],
               "7" => ["p", "q", "r", "s"],
               "8" => ["t", "u", "v"],
               "9" => ["w", "x", "y", "z"] }
   lc_recur(digits, combinations, mapping, "", 0)
    return combinations
end

p(letter_combinations("23"))
p(letter_combinations("13"))
p(letter_combinations("21"))
p(letter_combinations(""))
p(letter_combinations("1"))