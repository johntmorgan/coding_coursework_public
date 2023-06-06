class Node
  attr_accessor :children, :is_word
  def initialize()
    @children = {}
    @is_word = false
  end
end

class WordDictionary
  attr_accessor :root
  def initialize()
    @root = Node.new
  end

  def insert_word(word)
    node = @root
    word.each_char do |c|
      if node.children[c] == nil
        node.children[c] = Node.new
      end
      node = node.children[c]
    end
    node.is_word = true
  end

  def search_word(word)
    node = @root
    word.each_char do |c|
      if node.children[c] == nil
        return false
      else
        node = node.children[c]
      end
    end
    return node.is_word
  end
end