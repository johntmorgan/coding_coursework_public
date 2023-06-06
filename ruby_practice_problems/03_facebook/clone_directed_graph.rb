require './graph2.rb'

def rec_clone(node, visited)
  if node == nil
    return
  end

  new_node = Node.new(node.data)
  visited[node] = new_node

  node.neighbors.each do |neighbor|
    x = visited[neighbor]
    if x == nil
      new_node.neighbors += [rec_clone(neighbor, visited)]
    else
      new_node.neighbors += [x]
    end
  end
  return new_node
end

def clone(root_node)
  visited = {}
  return rec_clone(root_node, visited)
end

vertices = create_test_graph_directed(7, 18)
print_graph_rec(vertices[0])
cp = clone(vertices[0])

puts("\nAfter copy.")
print_graph(cp)