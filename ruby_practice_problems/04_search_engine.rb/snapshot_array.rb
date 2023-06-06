class SnapshotArray
  attr_accessor :arr, :snap_hash
  def initialize(length)
    @arr = [0] * length
    @snap_id = 0
    @snap_hash = {}
  end

  def set_value(idx, val)
    @arr[idx] = val
  end

  def snapshot()
    @snap_hash[@snap_id] = @arr.map(&:itself)
    @snap_id += 1
    return @snap_id - 1
  end

  def get_value(idx, snapid)
    if @snap_hash[snapid] == nil || idx > @snap_hash[snapid].length()
      return nil
    else
      return @snap_hash[snapid][idx]
    end
  end
end