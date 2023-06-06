
def group_anagrams(strs)
  encoded = {}
  strs.each do |str|
    code = [0] * 26
    str.each_char do |ch|
      idx = ch.ord - 'a'.ord
      code[idx] += 1
    end
    dict_code = code.join("")
    if encoded[dict_code] != nil
      encoded[dict_code].push(str)
    else
      encoded[dict_code] = [str]
    end
  end

  result = []
  encoded.keys().each do |key|
    result.push(encoded[key])
  end
  return result
end