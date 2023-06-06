def group_strings(strs)
    diffs = {}
    strs.each do |str|
        key = ""
        loc = 0
        while loc < str.length() - 1
            val = str[loc + 1].ord - str[loc].ord
            if val < 0
                val += 26
            end
            key += val.to_s
            loc += 1
        end
        if diffs[key] == nil
            diffs[key] = [str]
        else
            diffs[key].push(str)
        end
    end
    res = []
    diffs.keys().each do |key|
        group = diffs[key].sort()
        res.push(group)
    end
    result = res.sort()
    return result
end

strs = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "b", "y", "moqs"]
p(group_strings(strs))