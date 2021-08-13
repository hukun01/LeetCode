# 102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer[][]}
def level_order(root)
    return [] if root.nil?

    q = Queue.new()
    q.push(root)
    ans = []
    until q.empty?
        level = []
        (0...q.length).each do |_|
            node = q.pop
            level.push(node.val)
            q.push(node.left) unless node.left.nil?
            q.push(node.right) unless node.right.nil?
        end
        ans.push(level)
    end

    return ans
end