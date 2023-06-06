def count_connected_comp(edges, n)
    components = 0
    visited = []
    graph = {}
    edges.each do |edge|
      if graph[edge[0]] == nil
        graph[edge[0]] = [edge[1]]
      else
        graph[edge[0]] += [edge[1]]
      end
      if graph[edge[1]] == nil
        graph[edge[1]] = [edge[0]]
      else
        graph[edge[1]] += [edge[0]]
      end
    end
    edges.each do |edge|
      components += 1 if !visited.include?(edge[0]) && !visited.include?(edge[1])
      reachable = []
      reachable += [edge[0]] if !visited.include?(edge[0])
      reachable += [edge[1]] if !visited.include?(edge[1])
      while !reachable.empty?
        curr = reachable.shift()
        graph[curr].each do |point|
          if !visited.include?(point)
            visited.push(point)
            reachable.push(point)
          end
        end
      end
    end
    components += n - visited.length()
    return components
end


# Sample Input 1:
edges = [[0,1],[1,2],[3,4]]
n = 5
p(count_connected_comp(edges, n))

# Sample Input 2:
edges = [[0,1],[1,2],[2,3],[3,4]]
n = 5
p(count_connected_comp(edges, n))

edges = [[0,2],[1,3],[2,3]]
n = 4
p(count_connected_comp(edges, n))