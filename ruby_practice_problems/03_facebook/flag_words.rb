def repeated_letters(str, i)
    len = 0
    letter = str[i]
    while str[i] == letter
        i += 1
        len += 1
    end
    return len
end

def flag_words(str_S, str_W)
    if !str_S || !str_W
        return False
    end

    i, j = 0, 0
    while i < str_S.length() && j < str_W.length()
        if str_S[i] != str_W[j]
            return false
        else
            len1 = repeated_letters(str_S, i)
            len2 = repeated_letters(str_W, j)
            if len1 < 3 and len1 != len2 || len2 < 3 and len1 != len2
                return false
            end
            i += len1
            j += len2
        end
    end
    return i == str_S.length() && j = str_W.length()
end


str_S = "mooooronnn" # modified word
str_W = "moron" # original word

if flag_words(str_S, str_W)
    puts("Word Flagged")
    print("The word ", '"' + str_S + '"', " is a possible morph of ", '"' + str_W + '"')
else
    puts("Word Safe")
end
puts("")