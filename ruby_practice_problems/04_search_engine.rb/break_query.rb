# Time O(n^3) - two nested loops, substring computation at each iteration
# Space O(n) - n is query length, dp array length

def break_query(query, dict)
    n = query.length()
    dp = Array.new(n + 1, false)
    dp[0] = true
    for i in (0..n - 1)
        if dp[i]
            dict.each do |j|
                l = j.length()
                if i + l <= n && query[i...i + l] == j
                    dp[i + l] = true
                end
            end
        end
    end
    return dp[n]
end

query = "vegancookbook"
dict = ["i", "cream", "cook", "scream", "ice", "cat", "book", "icecream", "vegan"]
p(break_query(query, dict))

query = "veganicecream"
p(break_query(query, dict))

query = "veganicetea"
p(break_query(query, dict))