class Node
    attr_accessor :val, :key,:next, :prev
   def initialize(key, val)
       @val = val
       @key = key
       @next = nil
       @prev = nil
   end
end

class LinkedList
    attr_accessor :head, :tail, :size
    def initialize()
        @head = nil
        @tail = nil
        @size = 0
    end

    def insert_at_head(key, val)
        new_node = Node.new(key, val)
        if self.head == nil
            self.tail = new_node
            self.head = new_node
        else
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        end
        self.size+=1
    end

    def insert_at_tail(key, data)
        new_node = Node.new(key, data)
        if self.tail == nil
            self.tail = new_node
            self.head = new_node
            new_node.next = nil
        else
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = nil
        end

        self.size+=1
    end

    def remove_node(node)
        if node == nil
            return
        end

        if not node.prev == nil
            node.prev.next = node.next
        end

        if not node.next == nil
            node.next.prev = node.prev
        end

        if node == self.head
            self.head = self.head.next
        end

        if node == self.tail
            self.tail = self.tail.prev
        end
        self.size= self.size - 1

        return node
    end

    def remove_head()
        return self.remove_node(self.head)
    end

    def remove_tail()
        return self.remove_node(self.tail)
    end

    def get_head()
        return self.head
    end

    def get_tail()
        return self.tail
    end

end