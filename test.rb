# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end

    def visit_all(&block)
        visit(&block)
        left.visit_all(&block) unless left.nil?
        right.visit_all(&block) unless left.nil?
    end

    def visit(&block)
        block.call self
    end
end


ruby_tree = TreeNode.new("Ruby", TreeNode.new("LeftRuby"), TreeNode.new("RightRuby"))

puts "visiting a node"
ruby_tree.visit { |node| puts node.val }
puts

puts "visiting entire tree"

ruby_tree.visit_all { |node| puts node.val }