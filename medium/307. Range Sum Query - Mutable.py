# 307. Range Sum Query - Mutable

low_bit = lambda x: x & (-x)

class NumArray:
    '''
    Fenwick tree, Binary Indexed Tree (BIT).

    Let idx be an index of BIT. Let r be the position in idx of
    its last non-zero digit in binary notation, i.e., r is the position
    of the least significant non-zero bit of idx. tree[idx] holds the sum
    of frequencies in range [idx - 2^r + 1, idx].

    See more in https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees
    '''

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.tree = [0] * (n + 1)
        for i, a in enumerate(nums, start = 1):
            '''
            # Simpler update, but slower as O(logN).
            self.update(i-1, a)
            '''
            # O(1) update
            self.tree[i] += a
            if (parent_idx := i + low_bit(i)) <= n:
                self.tree[parent_idx] += self.tree[i]

    def update(self, i: int, val: int) -> None:
        dif = val - self.sumRange(i, i)
        i += 1
        while i < len(self.tree):
            self.tree[i] += dif
            i += low_bit(i)

    @staticmethod
    def query(tree, i):
        i += 1
        ans = 0
        while i >= 1:
            ans += tree[i]
            i -= low_bit(i)
        return ans

    def sumRange(self, i: int, j: int) -> int:
        return NumArray.query(self.tree, j) - NumArray.query(self.tree, i-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)