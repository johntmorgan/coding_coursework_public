class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.head != None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node

    def insert_last(self, x):
        new_node = Doubly_Linked_List_Node(x)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head == None:
            self.head = new_node

    def delete_first(self):
        x = self.head
        self.head = x.next
        self.head.prev = None
        return x.item

    def delete_last(self):
        x = self.tail
        self.tail = x.prev
        self.tail.next = None
        return x.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L1_front_end = x1.prev
        L1_back_end = x2.next
        L1_front_end.next = L1_back_end
        L1_back_end.prev = L1_front_end
        L2.head = x1
        L2.tail = x2
        L2.tail.next = None
        return L2

    def splice(self, x, L2):
        L1_end = x.next
        x.next = L2.head
        L2.head.prev = x
        L2.tail.next = L1_end
        L1_end.prev = L2.tail
        pass

## Fun with testing below

# DS = Doubly_Linked_List_Seq()
# DS.insert_last(5)
# print(DS)
# DS.insert_first(3)
# print(DS)
# DS.insert_first(6)
# print(DS)
# DS.insert_first(7)
# print(DS)
# DS.insert_last(9)
# print(DS)
# y = DS.delete_first()
# print(DS)
# print(y.item)
# z = DS.delete_last()
# print(DS)
# print(z.item)
# DS.insert_first(7)
# DS.insert_last(9)
# print(DS)
# i = 1
# x1 = DS.head.later_node(i)
# x2 = x1.next.next
# print(x1.item)
# print(x2.item)
# L2 = DS.remove(x1, x2)
# print(DS)
# print(L2)
# DS.insert_last(4)
# print(DS)
# x3 = DS.head.later_node(1)
# print(x3.item)
# DS.splice(x3, L2)
# print(DS)

# DS = Doubly_Linked_List_Seq()
# ans = []
# ops = [('insert_last', 3), ('insert_first', 2), ('insert_last', 8), ('insert_first', 2), ('insert_last', 9), ('insert_first', 7), ('delete_last',), ('delete_last',), ('delete_first',), ('splice/remove', 1, 2), ('splice/remove', 1, 2), ('splice/remove', 1, 2), ('splice/remove', 1, 2), ('splice/remove', 1, 2)]
# for op in ops:
#     print(*op)
#     if op[0] == "insert_first":
#         x = op[1]
#         DS.insert_first(x)
#     if op[0] == "insert_last":
#         x = op[1]
#         DS.insert_last(x)
#     if op[0] == "delete_first":
#         ans.append(DS.delete_first())
#     if op[0] == "delete_last":
#         ans.append(DS.delete_last())
#     if (op[0] == "splice/remove") and DS.head:
#         i, n = op[1], op[2]
#         L = Doubly_Linked_List_Seq()
#         L.build(range(n))
#         print('L: ', L)
#         x1 = DS.head.later_node(i)
#         x2 = x1.next
#         DS.splice(x1, L)
#         assert x2 != None
#         for _ in range(n):
#             L = DS.remove(x1.next, x2.prev)
#             x2 = x1.next
#             DS.splice(x1, L)
#     print(DS)
# ans.append(tuple([x for x in DS]))
# print(ans)