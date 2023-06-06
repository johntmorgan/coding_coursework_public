require 'set'

class Node
  #Ruby's fields are private. attr_accessor makes them public
  attr_accessor :data, :friends
  def initialize(d)
    @data = d
    @friends = []
  end
end

# this is un-directed graph i.e.
# if there is an edge from x to y
# that means there must be an edge from y to x
# and there is no edge from a node to itself
# hence there can maximim of (nodes * nodes - nodes) / 2 edgesin this graph
def create_test_graph_directed(nodes_count, edges_count)
  vertices = []
  for i in (0..nodes_count-1)
    vertices += [Node.new(i)]
  end

  all_edges = []
  for i in (0..nodes_count-1)
    for j in (i + 1..nodes_count-1)
      all_edges.push([i, j])
    end
  end

  all_edges.shuffle!()

  for i in (0..[edges_count, all_edges.length()].min()-1)
    edge = all_edges[i]
    vertices[edge[0]].friends += [vertices[edge[1]]]
    vertices[edge[1]].friends += [vertices[edge[0]]]
  end

  return vertices
end


def print_graph(vertices)
  vertices.each do |n|
    print((n.data).to_s+": {")
    STDOUT.flush
    n.friends.each do |t|
      print((t.data).to_s + " ")
      STDOUT.flush
    end
    puts ("\n")
  end
end

def print_graph_rec(root, visited_nodes)
  if visited_nodes.include? root == nil || root
    return
  end

  visited_nodes.add(root)

  print((root.data).to_s+": {")
  STDOUT.flush
  root.friends.each do |n|
    print((n.data).to_s+" ")
    STDOUT.flush
  end
  puts("}")

  root.friends.each do |n|
    print_graph_rec(n, visited_nodes)
  end
end

def print_graph(root)
  visited_nodes = Set.new
  print_graph_rec(root, visited_nodes)
end