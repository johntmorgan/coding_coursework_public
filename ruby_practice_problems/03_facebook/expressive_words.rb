
def expressive_words(str_S, words)
  count = 0
  words.each do |word|
    wp = 0
    sp = 0
    valid = true
    while sp < str_S.length()
      if str_S[sp] != word[wp]
        valid = false
        break
      else
        letter = str_S[sp]
        wl_count = 0
        sl_count = 0
        while wp < word.length() && word[wp] == letter
          wp += 1
          wl_count += 1
        end
        while sp < str_S.length() && str_S[sp] == letter
          sp += 1
          sl_count += 1
        end
        if sl_count < 3 && sl_count != wl_count
          valid = false
        end
      end
    end
    if valid && wp == word.length()
      count += 1
    end
  end
  return count
end


S = "tttttllll"
words = ["tl","tll","ttll","ttl"]
p(expressive_words(S, words))

S2 = "heeellooo"
words2 = ["hello", "hi", "helo"]
p(expressive_words(S2, words2))

S3 = "dddiiiinnssssssoooo"
words = ["dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso", "dinssoo", "dinso"]
p(expressive_words(S3, words))