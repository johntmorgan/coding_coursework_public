require './heap.rb'

def reorganize(str)
    freq = {}
    str.each_char do |chr|
        if freq[chr] == nil
            freq[chr] = 1
        else
            freq[chr] += 1
        end
    end
    heap = MaxHeap.new()
    freq.keys().each do |key|
        heap.push([freq[key], key])
    end
    reorg = ""
    while heap.size() > 0
        curr = heap.pop()
        if reorg.length() > 0 && curr[1] == reorg[-1]
            if heap.size() > 0
                other = heap.pop()
                reorg += other[1]
                heap.push(curr)
                if other[0] > 1
                    other[0] = other[0] - 1
                    heap.push(other)
                end
            else
                return ""
            end
        else
            reorg += curr[1]
            if curr[0] > 1
                curr[0] = curr[0] - 1
                heap.push(curr)
            end
        end
    end
    return reorg
end

str = "abaacdda"
p(reorganize(str))