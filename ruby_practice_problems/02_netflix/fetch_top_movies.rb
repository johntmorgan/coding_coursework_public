require './LinkedList.rb'

# O(n * k^2) - O(nk) - max list length * k number of lists
# Space O(1)

def merge2_country(l1, l2)
    dummy = Node.new(-1)
    curr = dummy

    while l1 and l2
        if l1.value <= l2.value
            curr.next = l1
            l1 = l1.next
        else
            curr.next = l2
            l2 = l2.next
        end
        curr = curr.next
    end

    if l1 != nil
        curr.next = l1
    else
        curr.next = l2
    end
    return dummy.next
end

def mergeK_country(lists)
    if lists.length() > 0
        res = lists[0]
        (1..lists.length() - 1).each do |i|
            res = merge2_country(res, lists[i])
        end
        return res
    end
    return nil
end

a = create_linked_list([11,41,51])
b = create_linked_list([21,23,42])
c = create_linked_list([25,56,66,72])

puts "Result:"
display(mergeK_country([a, b, c]))