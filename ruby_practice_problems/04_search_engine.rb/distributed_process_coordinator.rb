# Time snap() O(n), fetch & set O(1)
# Space O(n * m) - number of nodes times number of saved states

class Snapshot
  attr_accessor :arr_size, :snapshot_id, :node_state
  def initialize(length)
    @snap_id = 0
    @node_state = Hash.new
    @node_state[0] = Hash.new
    @arr_size = length
  end

  def set_state(idx, val)
    if idx < @arr_size
      @node_state[@snap_id][idx] = val
    end
  end

  def snap()
    @snap_id += 1
    @node_state[@snap_id] = @node_state[@snap_id - 1].clone()
    return @snap_id - 1
  end

  def fetch_state(idx, snap_id)
    if snap_id < @snap_id && snap_id >= 0 && idx < @arr_size
      if @node_state[@snap_id].include? idx
        return @node_state[@snap_id][idx]
      else
        return 0
      end
    else
      return nil
    end
  end
end

puts("-----Example 1:-----")
puts("")
snapshotArr = Snapshot.new(3)
puts("Initializing the data structure with three nodes")
puts("Setting the state of node 0 to 5")
snapshotArr.set_state(0,5)
puts("Snap id: " + snapshotArr.snap().to_s)
snapshotArr.set_state(0,1)
puts("Setting the state of node 0 to 1")
snapshotArr.set_state(2,3)
puts("Setting the state of node 2 to 3")
snapshotArr.set_state(1,10)
puts("Setting the state of node 1 to 10")
puts("Node state at index 0 with Snap id 0 is: " + (snapshotArr.fetch_state(0,0)).to_s)
puts("Snap id: " + snapshotArr.snap().to_s)
puts("Node state at index 0 with Snap id 1 is: " + snapshotArr.fetch_state(0,1).to_s)
puts("Node state at index 1 with Snap id 1 is: " + snapshotArr.fetch_state(1,1).to_s)

puts("")
puts("-----Example 2:-----")
puts("")
snapshotArr = Snapshot.new(5)
puts("Initializing the data structure with five nodes")
puts("Setting the state of node 4 to 1")
snapshotArr.set_state(4,1)
puts("Snap id: " + snapshotArr.snap().to_s)
snapshotArr.set_state(2,21)
puts("Setting the state of node 2 to 21")
puts("Snap id: " + snapshotArr.snap().to_s)
puts("Node state at index 4 with Snap id 1 is: " + (snapshotArr.fetch_state(4,1)).to_s)
puts("Node state at index 2 with Snap id 1 is: " + (snapshotArr.fetch_state(2,1)).to_s)
puts("Node state at index 3 with Snap id 1 is: " + (snapshotArr.fetch_state(3,1)).to_s)