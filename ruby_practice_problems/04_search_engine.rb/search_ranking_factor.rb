# O(n) time complexity
# O(n) space complexity

def search_ranking(page_scores)
  length = page_scores.length()
  ranking = [0] * length
  ranking[0] = 1
  (1..length - 1).each do |i|
    ranking[i] = page_scores[i - 1] * ranking[i - 1]
  end
  right = 1;
  (0...length).reverse_each do |i|
    ranking[i] = ranking[i] * right
    right *= page_scores[i]
  end
  return ranking
end

page_scores = [3, 5, 1, 1, 6, 7, 2, 3, 4, 1, 2]
p(search_ranking(page_scores))