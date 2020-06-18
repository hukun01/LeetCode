# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        tree = defaultdict(list)
        i = 0
        while i < len(S):
            j = i
            while j < len(S) and S[j] == '-':
                j += 1
            depth = j - i
            i = j
            while j < len(S) and S[j].isdigit():
                j += 1
            num = int(S[i:j])
            i = j
            tree[depth].append(TreeNode(num))
            if depth - 1 >= 0:
                parent = tree[depth - 1][-1]
                if not parent.left:
                    parent.left = tree[depth][-1]
                else:
                    parent.right = tree[depth][-1]
        if not tree:
            return None
        return tree[0][0]