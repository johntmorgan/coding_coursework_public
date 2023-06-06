def min_window(main, target)
    best = ""
    len_best = Float::INFINITY
    freq = {}
    right, left = 0, 0
    target_hash = {}
    target.each_char do |char|
        if target_hash[char] == nil
            target_hash[char] = 1
        else
            target_hash[char] += 1
        end
    end
    while right < main.length()
        letter = main[right]
        if freq[letter] == nil
            freq[letter] = 1
        else
            freq[letter] += 1
        end
        valid = true
        target_hash.keys().each do |key|
            if freq[key] == nil || target_hash[key] > freq[key]
                valid = false
            end
        end
        check = true if valid == true
        while valid == true
            target_hash.keys().each do |key|
                if freq[key] == nil || target_hash[key] > freq[key]
                    valid = false
                end
            end
            p(left, right, freq, target_hash)
            if valid && left < main.length()
                freq[main[left]] -= 1
                left += 1
            else
                left -= 1
                freq[main[left]] += 1
            end
        end
        if check
            curr_len = right - left + 1
            if curr_len < len_best
                len_best = curr_len
                best = main.slice(left, curr_len)
            end
        end
        right += 1
    end
    return best
end

string_s = "ABAACBBA"
string_t = "AABC"
p(min_window(string_s, string_t))

# string_s = "ABAACBAB"
# string_t = "ABCC"
# p(min_window(string_s, string_t))