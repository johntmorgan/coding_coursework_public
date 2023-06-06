def max_sub_array(arr)
    max_sum = -Float::INFINITY
    best_arr = []
    arr.each_with_index do |num, i|
        if i == 0
            best = num
        else
            best = [num, num + best_arr[i - 1]].max()
        end
        max_sum = best if best > max_sum
        best_arr.push(best)
    end
    return max_sum
end

arr = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
p(max_sub_array(arr))