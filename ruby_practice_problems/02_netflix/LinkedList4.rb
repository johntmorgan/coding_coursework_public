class LinkedListNode
  #Ruby's fields are private. But, attr_accessor makes them public
  attr_accessor :next, :prev, :arbitrary, :data
  def initialize(data)
    @data = data
    @next = nil
    @prev = nil
    @arbitrary = nil
  end
end


def insert_at_head(head, data)
  newNode = LinkedListNode.new(data)
  newNode.next = head
  return newNode
end


def insert_at_tail(head, node)
  if head == nil
    return node
  end

  temp = head;

  while temp.next != nil
    temp = temp.next
  end

  temp.next = node;
  return head
end


def create_random_list(length)
  list_head = nil
  for i in (0..length-1)
    list_head = insert_at_head(list_head, random.randrange(1, 100))
  end
  return list_head
end

def create_linked_list(lst)
  list_head = nil
  lst.reverse.each do |x|
    list_head = insert_at_head(list_head, x)
  end
  return list_head
end

def display(head)
  temp = head
  while temp
    print(String(temp.data))
    STDOUT.flush
    temp = temp.next
    if temp != nil
      print(", ")
      STDOUT.flush
    end
  end
end

def to_list(head)
  lst = []
  temp = head
  while temp
    lst.push(temp.data)
    temp = temp.next
  end
  return lst
end

def is_equal(list1, list2)
  if list1 == list2
    return true
  end

  while list1 != nil && list2 != nil
    if list1.data != list2.data
      return false
    end
    list1 = list1.next
    list2 = list2.next
  end

  return list1 == list2
end