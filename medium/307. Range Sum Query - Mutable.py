# 307. Range Sum Query - Mutable
class NumArray:
    '''
    1/2 Fenwick tree, Binary Indexed Tree (BIT).

    Let idx be an index of BIT. Let r be the position in idx of
    its last non-zero digit in binary notation, i.e., r is the position
    of the least significant non-zero bit of idx. tree[idx] holds the sum
    of frequencies in range [idx - 2^r + 1, idx].

    See more in https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees
    '''

    def __init__(self, nums: List[int]):
        self.bit = BinaryIndexedTree(len(nums))
        self.bit.initialize(nums)

    def update(self, i: int, val: int) -> None:
        dif = val - self.sumRange(i, i)
        self.bit.update(i+1, dif)

    def sumRange(self, i: int, j: int) -> int:
        return self.bit.getPrefixSum(j+1) - self.bit.getPrefixSum(i)

class BinaryIndexedTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    # O(n) initialization. Better than using update() which leads to O(Ologn).
    def initialize(self, nums):
        assert len(nums) + 1 == len(self.sums)
        
        for i, a in enumerate(nums, start = 1):
            self.sums[i] += a
            if (parent_idx := i + self.low_bit(i)) <= len(nums):
                self.sums[parent_idx] += self.sums[i]
        
    def low_bit(self, i):
        return i & (-i)
        
    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += val
            i += self.low_bit(i)
    
    def getPrefixSum(self, i):
        ans = 0
        while i > 0:
            ans += self.sums[i]
            i -= self.low_bit(i)
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

class NumArray:
    '''
    2/2 Segment Tree (basic form with dynamic insert)
    No lazy propagation, no discretization. Just update_single (update_range)
    and query_range.
    '''

    def __init__(self, nums: List[int]):
        self.tree = SegTreeNode(0, len(nums))
        for i, a in enumerate(nums):
            self.tree.insert(i, a)


    def update(self, index: int, val: int) -> None:
        self.tree.insert(index, val)


    def sumRange(self, left: int, right: int) -> int:
        return SegTreeNode.query_range_sum(self.tree, left, right)


class SegTreeNode:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.left = self.right = None
        self.sum = 0


    def insert(self, p, val):
        if not self.a <= p <= self.b:
            return

        if self.a == p == self.b:
            self.sum = val
            return

        m = (self.a + self.b) // 2
        self.left = self.left or SegTreeNode(self.a, m)
        self.right = self.right or SegTreeNode(m + 1, self.b)

        self.left.insert(p, val)
        self.right.insert(p, val)

        self.sum = self.left.sum + self.right.sum


    @staticmethod
    def query_range_sum(node, a, b):
        if node.a > b or node.b < a:
            return 0

        if node.a >= a and node.b <= b:
            return node.sum

        return SegTreeNode.query_range_sum(node.left, a, b) + SegTreeNode.query_range_sum(node.right, a, b)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)