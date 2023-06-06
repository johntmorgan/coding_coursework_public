class Tree
    attr_accessor :val, :left, :right
    def initialize(val=0, left=nil, right=nil)
        @val = val
        @left = left
        @right = right
    end
end

# class ConstructBinaryTree
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

    def build_binary_tree(preorder, inorder)
        inorder_val_idx = {}
        inorder.each_with_index do |val, i|
            inorder_val_idx[val] = i
        end
        return create_tree_from_val(0, preorder.length() - 1, preorder, inorder_val_idx, 0)
    end

    # def create_tree_from_val(left, right, curr, preorder, inorder_val_idx)
    #     p([left, right])
    #     if left > right || curr > preorder.length() || inorder_val_idx[preorder[curr]] == nil
    #         return nil
    #     end
    #     node_val = preorder[curr]
    #     node = Tree.new(node_val)
    #     idx = inorder_val_idx[node_val]
    #     p(idx)
    #     node.left = create_tree_from_val(0, idx - 1, 2 * curr + 1, preorder, inorder_val_idx)
    #     node.right = create_tree_from_val(idx + 1, right, 2 * curr + 2, preorder, inorder_val_idx)
    #     return node
    # end

    # def build_binary_tree(preorder, inorder)
    #     if preorder.length() == 0
    #         return nil
    #     end
    #     inorder_val_idx = {}
    #     inorder.each_with_index do |val, idx|
    #         inorder_val_idx[val] = idx
    #     end
    #     p(inorder_val_idx)
    #     return create_tree_from_val(0, preorder.length() - 1, 0, preorder, inorder_val_idx)
    # end
# end

p(build_binary_tree([3, 9, 20, 15, 7],[9, 3, 15, 20, 7]))
