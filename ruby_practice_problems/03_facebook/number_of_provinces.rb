def dfs_province(is_connected, visited, ri, ci)
  ri = ci
  row = is_connected[ri]
  (0...row.length()).each do |ci|
    if is_connected[ri][ci] == 1 && !visited.include?(ci)
      visited.push(ci)
      dfs_province(is_connected, visited, ri, ci)
    end
  end
end

def find_provinces_num(is_connected)
  provinces = 0
  visited = []
  (0...is_connected.length()).each do |ri|
    provinces += 1 if ! visited.include?(ri)
    (0...is_connected[0].length()).each do |ci|
      if is_connected[ri][ci] == 1 && !visited.include?(ci)
        visited.push(ci)
        dfs_province(is_connected, visited, ri, ci)
      end
    end
  end
  return provinces
end

is_connected = [[1,1,0],[1,1,0],[0,0,1]]
p(find_provinces_num(is_connected))

is_connected = [[1,0,0],[0,1,0],[0,0,1]]
p(find_provinces_num(is_connected))

is_connected = [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]
p(find_provinces_num(is_connected))