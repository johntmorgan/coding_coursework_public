require './LinkedList4.rb'

def merge_k_lists(lists)
  while lists.length() > 1
    l1 = lists.shift
    l2 = lists.shift
    dummy = LinkedListNode.new(-1)
    curr = dummy

    while l1 && l2
      if l1.data <= l2.data
        curr.next = l1
        l1 = l1.next
      else
        curr.next = l2
        l2 = l2.next
      end
      curr = curr.next
    end

    curr.next = l1 if l1
    curr.next = l2 if l2
    lists.push(dummy.next)
  end

  return lists[0]
end

