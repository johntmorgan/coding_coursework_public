# Netflix mantains popularity score for each title
# Want to identify consistently increasing and decreasing titles

# Time O(n)
# Space O(1)

def identify_titles(movie_rating)
  increasing, decreasing = true, true
  movie_rating[0...-1].each_with_index do |_, i|
    if movie_rating[i] < movie_rating[i + 1]
      decreasing = false
    elsif movie_rating[i] > movie_rating[i + 1]
      increasing = false
    end
  end
  return increasing || decreasing
end


# Driver code
movie_ratings = [
    [1,2,2,3],
    [4,5,6,3,4],
    [8,8,7,6,5,4,4,1]
]

movie_ratings.each_with_index do |movie_rating, i|
    puts "Movie index: #{i}"
    if identify_titles(movie_rating)
        puts("Title Identified and Separated")
    else
        puts("Title Score Fluctuating")
    end
end