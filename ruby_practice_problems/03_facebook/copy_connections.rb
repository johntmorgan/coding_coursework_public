require './graph.rb'

def rec_clone(node, visited)
  if node == nil
    return
  end

  new_node = Node.new(node.data)
  visited[node] = new_node

  node.friends.each do |friend|
    x = visited[friend]
    if x == nil
      new_node.friends += [rec_clone(friend, visited)]
    else
      new_node.friends += [x]
    end
  end
  return new_node
end

def clone_graph(root)
  visited = {}
  return rec_clone(root, visited)
end

vertices = create_test_graph_directed(7, 18)
print_graph(vertices[0])
cp = clone_graph(vertices[0])

puts("\nAfter copy.")
print_graph(cp)