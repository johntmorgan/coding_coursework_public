# O(n) time to build hashmap, O(n) time to build tree
# O(n) space - hashmap

class Node
    attr_accessor :val, :left, :right
    def initialize(val=0, left=nil, right=nil)
        @val = val
        @left = left
        @right = right
    end
end

class ConstructBinaryTree
    def create_tree_from_val(left, right, preorder, inorder_val_idx, node_index)
        if left > right || node_index >= preorder.length()
            return nil
        end
        node_val = preorder[node_index]
        node = Node.new(node_val)
        p([node_index, node_val, inorder_val_idx])
        node.left = create_tree_from_val(left, inorder_val_idx[node_val] - 1, preorder, inorder_val_idx, 2 * node_index + 1)
        node.right = create_tree_from_val(inorder_val_idx[node_val] + 1, right, preorder, inorder_val_idx, 2 * node_index + 2)
        return node
    end

    def re_creating_decision_tree(preorder, inorder)
        inorder_val_idx = {}
        inorder.each_with_index do |val, i|
            inorder_val_idx[val] = i
        end
        return create_tree_from_val(0, preorder.length() - 1, preorder, inorder_val_idx, 0)
    end
end


# Driver Code
preorder = ["subject", "viewed", "notviewed", "similar", "nonsimilar"]
inorder = [ "viewed", "subject", "similar", "notviewed", "nonsimilar" ]

obj = ConstructBinaryTree.new
tree = obj.recreate_decision_tree(preorder, inorder )
count = 10
display_tree(tree)
