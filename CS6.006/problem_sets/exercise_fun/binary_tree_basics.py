#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:40:17 2022

@author: johnmorgan
"""

def height(A):
    if A: return A.height
    else: return -1

class Binary_Node():
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        A.subtree_update()

    def subtree_update(A): # O(1)
        A.height = 1 + max(height(A.left), height(A.right))

    def skew(A):
        return height(A.right) - height(A.left)

    def subtree_iter(A):
        if A.left: yield from A.left.subtree_iter()
        yield(A)
        if A.right: yield from A.right.subtree_iter()
    
    def subtree_first(A):
        if A.left:  return A.left.subtree_first()
        else:       return A
    
    def subtree_last(A):
        if A.right: return A.right.subtree_last()
        else:       return A
    
    def successor(A):
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent
    
    def predecessor(A):
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent
    
    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        A.maintain()
    
    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
        A.maintain()

    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else:      B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else:                  A.parent.right = None
            A.parent.maintain()
        return A

    def subtree_rotate_right(D):
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def subtree_rotate_left(B):
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def rebalance(A):
        if A.skew() == 2:
            if A.right.skew() < 0:
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew == -2:
            if A.left.skew() > 0:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()
    
    def maintain(A):
        A.rebalance()
        A.subtree_update()
        if A.parent: A.parent.maintain()

class Binary_Tree:
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type

    def __len__(T): return T.size
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item

class BST_Node(Binary_Node):
    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        # A.maintain()

    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
        # A.maintain()

    def subtree_find(A, k): # O(h)
        if k < A.item:
            if A.left: return A.left.subtree_find(k)
        elif k > A.item:
            if A.right: return A.right.subtree_find(k)
        else: return A
        return None

    def subtree_find_next(A, k): # O(h)
        if A.item <= k:
            if A.right: return A.right.subtree_find_next(k)
            else: return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            if B: return B
        return A

    def subtree_find_prev(A, k): # O(h)
        if A.item >= k:
            if A.left: return A.left.subtree_find_prev(k)
            else: return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B: return B
        return A

    def subtree_insert(A, B): # O(h)
        if B.item < A.item:
            if A.left: A.left.subtree_insert(B)
            else: A.subtree_insert_before(B)
        elif B.item > A.item:

            if A.right: A.right.subtree_insert(B)
            else: A.subtree_insert_after(B)
        else:
            A.item = B.item
        
class Set_Binary_Tree(Binary_Tree): # Binary Search Tree
    def __init__(self): super().__init__(BST_Node)
    
    def iter_order(self): yield from self

    def build(self, X):
        for x in X: self.insert(x)

    def find_min(self):
        if self.root: 
            return self.root.subtree_first().item

    def find_max(self):
        if self.root:
            return self.root.subtree_last().item

    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node: return node.item
    
    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node: return node.item

    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node: return node.item

    def insert(self, x):
        new_node = self.Node_Type(x)
        if self.root != None:
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False
        else:
            self.root = new_node
        self.size += 1
        return True
    
    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item

bst = Set_Binary_Tree()
bst.build(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
bst.insert('H')
print(bst.find_max())

class Size_Node(Binary_Node):
    def subtree_update(A):
        super().subtree_update()
        A.size = 1
        if A.left:  A.size += A.left.size
        if A.right: A.size += A.right.size
    
    def subtree_at(A, i):
        assert 0 <= i
        if A.left:       L_size = A.left.size
        else:            L_size = 0
        if i < L_size:   return A.left.subtree_at(i)
        elif i > L_size: return A.right.subtree_at(i - L_size - 1) 
        else:            return A

# Not working ugh - not sure what code they did not give me
class Seq_Binary_Tree(Binary_Tree):
    def __init(self): super().__init__(Size_Node)
    
    def build(self, X):
        def build_subtree(X, i, j):
            c = (i + j) // 2
            # modified from A[c] - think that was a typo
            root = self.Node_Type(X[c])
            if i < c:
                root.left = build_subtree(X, i, c - 1)
                root.left.parent = root
            if c < j:
                root.right = build_subtree(X, c + 1, j)
                root.right.parent = root
            root.subtree_update()
            return root
        self.root = build_subtree(X, 0, len(X) - 1)
        self.size = self.root.size
            
    def get_at(self, i):
        assert(self.root)
        return self.root.subtree_at(i).item

    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).items

    def insert_at(self, i, x):
        new_node = self.Node_Type(x)
        if i == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:
                self.root = new_node
        else:
            node = self.root.subtree_at(i - 1)
            node.subtree_insert_after(new_node)
        self.size += 1
        
    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item
    
    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self):    return self.delete_at(0)
    def insert_last(self, x):  self.insert_at(len(self))
    def delete_last(self):     return self.delete_at(len(self) - 1)

T = Seq_Binary_Tree()
T.build([10,6,8,5,1,3])

# def create_tree():
#     a = Binary_Node('A')
#     b = Binary_Node('B')
#     c = Binary_Node('C')
#     d = Binary_Node('D')
#     a.left, b.parent = b, a
#     a.right, c.parent = c, a
#     c.left, d.parent = d, c
#     # print(subtree_first(a).item)
#     print(a.successor().item)
#     print(d.successor().item)
#     print(a.predecessor().item)
#     print(d.predecessor().item)
#     e = Binary_Node('E')
#     d.subtree_insert_after(e)
#     print(d.successor().item)
#     f = Binary_Node('F')
#     a.subtree_insert_before(f)
#     print(a.predecessor().item)
#     print(f.subtree_delete().item)
#     print(a.predecessor().item)
  
# create_tree()  
  

# def build(X):
#     A = [x for x in X]
#     def build_subtree(A, i ,j):
#         c = (i + j) // 2
#         root = self.Node_Type(A[c])
#         if i < c:
#             root.left = build_subtree(A, i, c - 1)
#             root.left.parent = root
#         if c < j:
#             root.right = build_subtree(A, c + 1, j)
#             root.right.parent = root
#         return root
#     self.root = build_subtree(A, 0, len(A) - 1)


    
