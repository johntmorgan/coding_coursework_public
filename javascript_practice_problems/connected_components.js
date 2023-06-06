function count_connected_comp(edges, n) {
  var components = 0;
  var visited = [];
  var graph = {};
  for (index in edges) {
    edge = edges[index];
    if (graph[edge[0]] == null)
      graph[edge[0]] = [edge[1]]
    else
      graph[edge[0]].push(edge[1])
    if (graph[edge[1]] == null)
      graph[edge[1]] = [edge[0]]
    else
      graph[edge[1]].push(edge[0])
  }
  for (index in edges) {
    edge = edges[index]
    if (visited[edge[0]] == null && visited[edge[1]] == null) {
      components += 1;
    }
    reachable = []
    if (visited[edge[0]] == null)
      reachable.push(edge[0])
    if (visited[edge[1]] == null)
      reachable.push(edge[1])
    while (reachable.length > 0) {
      curr = reachable.shift();
      for (index in graph[curr]) {
        point = graph[curr][index]
        if (!visited.includes(point)) {
          visited.push(point);
          reachable.push(point);
        }

      }
    }
  }
  components += n - visited.length
  return components
}



edges = [[0,1],[1,2],[3,4]]
n = 5
console.log(count_connected_comp(edges, n));

edges = [[0,1],[1,2],[2,3],[3,4]]
n = 5
console.log(count_connected_comp(edges, n));

edges = [[0,2],[1,3],[2,3]]
n = 4
console.log(count_connected_comp(edges, n));