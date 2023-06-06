
# Time O(k^n * n) - k max length of genre, n number of genres
# Space O(nk) space

def backtrack(index, path, categories, movies, combinations)
    if path.length() == categories.length()
        combinations.push(path.join(""))
        return
    end

    possible_movies = movies[categories[index]]
    if possible_movies != nil
        possible_movies.each do |pm|
            path.push(pm + ";")
            backtrack(index + 1, path, categories, movies, combinations)
            path.pop()
        end
    end
end

def letter_combinations(categories)
    # If the input is empty, immediately return an empty answer array
    if categories.length() == 0
        return []
    end

    #  Mapping the categories to their corresponding movies
    movies = {
    "Family" => ["Frozen","Kung fu Panda", "Ice Age"],
    "Action" => ["Iron Man","Wonder Woman","Avengers"],
    "Fantasy" => ["Jumangi", "Lion King", "Tarzan"],
    "Comedy" => ["Coco", "The Croods", "Vivi","Pets"],
    "Horror" => ["Oculus", "Sinister","Insidious","Annebelle"] }

    # Initiate backtracking with an empty path and starting index of 0
    combinations = []
    backtrack(0, [], categories, movies, combinations)
    return combinations
end

#Example 1
categories = ["Action"]
combinations = letter_combinations(categories)
output = combinations.join(',')
puts("Output 1:")

puts(output)

# Example 2
categories = ["Family", "Action"]
combinations = letter_combinations(categories)
output = combinations.join(', ')
puts("Output 2:")
puts(output)

# Example 3
categories = ["Horror", "Comedy"]
combinations = letter_combinations(categories)
output = combinations.join(', ')
puts("Output 3:")
puts(output)


# Example 4
categories = ["Horror", "Fantasy", "Comedy", "Family"]
combinations = letter_combinations(categories)
output = combinations.join(', ')
puts("Output 4:")
puts(output)
