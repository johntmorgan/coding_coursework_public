def dfs_island(islands, row_index, col_index)
  if row_index > 0 && islands[row_index - 1][col_index] == "1"
    islands[row_index - 1][col_index] = "0"
    dfs_island(islands, row_index - 1, col_index)
  end
  if row_index < islands.length() - 1 && islands[row_index + 1][col_index] == "1"
    islands[row_index + 1][col_index] = "0"
    dfs_island(islands, row_index + 1, col_index)
  end
  if col_index > 0 && islands[row_index][col_index - 1] == "1"
    islands[row_index][col_index - 1] = "0"
    dfs_island(islands, row_index, col_index - 1)
  end
  if col_index < islands[0].length() - 1 && islands[row_index][col_index + 1] == "1"
    islands[row_index][col_index + 1] = "0"
    dfs_island(islands, row_index, col_index + 1)
  end
end

def num_islands(islands)
  num_islands = 0
  (0...islands.length()).each do |row_index|
    (0...islands[0].length()).each do |col_index|
      if islands[row_index][col_index] == "1"
        num_islands += 1
        islands[row_index][col_index] = "0"
        dfs_island(islands, row_index, col_index)
      end
    end
  end
  return num_islands
end


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
p(num_islands(grid))