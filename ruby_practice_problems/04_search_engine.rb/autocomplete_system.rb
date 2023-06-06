# Time
# O(n * l) constructor - traverse n records of average length l to create trie
# O(q + m + [l * logl]) auto_complete - a is length of string, m is nodes in trie
# then l * log(l) to sort list of queries for top 3

# Space
# O(n * l) space - constructor storing n records of length l
# O(n * l) space for auto_complete() - n records of average length l stored in list to return

class Node
  attr_accessor :children, :is_end, :data, :rank
  def initialize()
    @children = {}
    @is_end = false
    @data = nil
    @rank = 0
  end
end

class AutocompleteSystem

  attr_accessor :keyword, :root
  def initialize(sentences, times)
    @root = Node.new()
    @keyword = ""
    sentences.each_with_index do |sentence, i|
      add_record(sentence, times[i])

    end
  end

  def add_record(sentence, hot)
    k = @root
    sentence.each_char do |c|
      if !k.children.include? c
        k.children[c] = Node.new
      end
      k = k.children[c]
    end
    k.is_end = true
    k.data = sentence
    k.rank -= hot
  end

  def dfs(node)
    ret = []
    if node.is_end == true
      ret.push([node.rank, node.data])
    end
    node.children.each do |child|
      ret.concat(dfs(node.children[child[0]]))
    end
    return ret
  end

  def search(sentence)
    k = @root
    sentence.each_char do |c|
      if !k.children.include? c
        return []
      end
      k = k.children[c]
    end
    return dfs(k)
  end

  def autoComplete(c)
    results = []
    if c != "#"
      @keyword += c
      results = search(@keyword)
    else
      add_record(@keyword, 1)
      @keyword = ""
    end

    ret = []
    for item in results.sort()[0...3]
      ret.push(item[1])
    end

    return ret
  end
end

sentences = ["beautiful", "best quotes", "best friend", "best birthday wishes", "instagram", "internet"]
times = [30, 14, 21, 10, 10, 15]
auto = AutocompleteSystem.new(sentences, times)
p(auto.autoComplete("b"))
p(auto.autoComplete("e"))
p(auto.autoComplete("s"))
p(auto.autoComplete("t"))
p(auto.autoComplete("#"))