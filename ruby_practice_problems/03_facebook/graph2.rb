require 'set'

class Node
  attr_accessor :data, :neighbors
  def initialize(d)
    @data = d
    @neighbors = []
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
    vertices[edge[0]].neighbors += [vertices[edge[1]]]
    vertices[edge[1]].neighbors += [vertices[edge[0]]]
  end

  return vertices
end


def get_graph1(vertices)
  gr = ""
  vertices.each do |n|
    gr += (n.data).to_s + ": {"
    n.neighbors.each do |t|
      gr+= (t.data).to_s + " "
    end
  end
  return gr
end

def print_graph_rec(root, visited_nodes,gr)
  if (visited_nodes.include? root) || (root==nil)

    return nil
  end

  visited_nodes.add(root)

  st = ""
  st+= (root.data).to_s + ": {"
  root.neighbors.each do |n|
    st += (n.data).to_s + " "
  end

  st+= "}"
  gr.push(st)

  root.neighbors.each do |n|
    print_graph_rec(n, visited_nodes,gr)
  end
end

def get_graph2(root)
  visited_nodes = Set.new
  gr = []
  print_graph_rec(root, visited_nodes,gr)
  return gr
end