class LinkedListNode
    #Ruby's fields are private. attr_accessor makes them public
    attr_accessor :key, :prev, :val, :next, :freq
    def initialize(key, value, freq)
        @key = key
        @val = value
        @freq = freq
        @next = nil
        @prev = nil
    end
end


class LinkedList
    #Ruby's fields are private. attr_accessor makes them public
    attr_accessor :head, :tail
    def initialize()
        @head = nil
        @tail = nil
    end

    def append(node)
        node.next, node.prev = nil, nil
        if @head == nil
            @head = node
        else
            @tail.next = node
            node.prev = @tail
        end
        @tail = node
    end

    def delete(node)
        if node.prev
            node.prev.next = node.next
        else
            @head = node.next
        end
        if node.next
            node.next.prev = node.prev
        else
            @tail = node.prev
        end
        node.next, node.prev = nil, nil
    end
end

