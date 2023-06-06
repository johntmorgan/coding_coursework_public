def traverse(root)
  res = []
  level = []
  queue = [root, "level"]
  while !queue.empty?
    node = queue.shift
    if node == "level"
      res.push(level.map(&:itself))
      level = []
      queue.push("level") if !queue.empty?
    else
      queue.push(node.left) if node.left
      queue.push(node.right) if node.right
      level.push(node.val)
    end
  end
  res
end