# 218. The Skyline Problem
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        1/2 Sort + Priority queue.
        Scan through the sorted buildings, and compare each one with the
        current heighest building in effect, record if there's a difference.

        For each building, it has two intervals, one is [left, height, right],
        another is [right, 0, inf]. We need the second one to tell when the
        building is out of scope, and to record the key point on the bottom
        right of the last building. We sort this interval list, so we can scan
        through it from left to right. Note that we make the height to negative
        so the max ones come first when the left boundaries are the same.

        As we scan through the building intervals, use a heap to record the
        current max height and its boundary. If the heap boundary is outside
        of or on the current building interval's left boundary, we keep poping
        the current max height out. If there's a non-0 height from the
        interval, it's a new building coming into the scope, we add it to the
        heap. Whenever the latest skyline key point has different height than
        the current max height, we add the new key point using current max.
        Note that we initialize the heap with (0, inf), meaning 0 height always
        exists.

        Time: O(n log(n)) where n is len(buildings). This comes from sorting
              the interval list. Same time is taken on scanning through the
              intervals, and do at most n heap push and pop, respectively,
              each of which takes O(log(n)).
        Space: O(n)
        '''
        boundaries = []
        for l, r, h in buildings:
            boundaries.append((l, -h, r))
            boundaries.append((r, 0, inf))

        boundaries.sort()
        heights_boundary = [(0, inf)] # (height, ending_boundary)
        skyline = []
        for start, neg_h, end in boundaries:
            while heights_boundary[0][1] <= start:
                heappop(heights_boundary)
            if neg_h != 0:
                heappush(heights_boundary, (neg_h, end))
            cur_max_height = -heights_boundary[0][0]
            if not skyline or skyline[-1][1] != cur_max_height:
                skyline.append([start, cur_max_height])
        return skyline
        '''
        2/2 Segment Tree (range maximum query).
        The problem is straightforward if we look at it in a brute force way:
        we just find the max height and its x coordinate from each point, and
        record that point's x and height if the height is different than the
        previous point.

        We can model each point as a node in a Segment Tree, and finding the
        max from a point takes O(log(n)) time. Before that, we need to address
        below challenges:
        1. Efficient range update. We need to use lazy propagation technique to
           make range update O(log(n)) time.
        2. Discretization. The *value* space is huge (2 ^31), but the totoal
           building length is reasonably small (10 ^ 4). Hence, instead of
           tracking every possible x value, we map each unique building
           interval start and end to an unique index. And our segment tree
           just need to track the index space, aka, at most 10 ^ 4 nodes.

        After building the building position to index mapping, and the tree,
        we just do a dfs to find each leaf node's start (index) and height.
        If the height is different than the previous height, we collect it in
        the answer.

        Note: the input data can be organized in a way that makes lazy
        propagation ineffective. E.g., given [[1,10001,10000],[2,10001,9999]],
        we first update range [1, 10001] with 10000 lazy value, assuming it
        went down to depth D; and secondly we update range [2, 10001] with
        9999, we need to go down to near to depth D again, because the new
        value is smaller and it could impact different children nodes. This
        way, the lazy update isn't really working.
        To handle this issue, we sort the buildings by height, so we always
        stop as early as possible, leveraging lazy update.

        Time: O(n log(n))
        Space: O(n)
        '''
        pos = set()
        for l, r, h in buildings:
            pos |= {l, r}

        idx2pos = sorted(pos)
        pos2idx = {p: i for i, p in enumerate(idx2pos)}

        n = len(idx2pos)
        root = SegTreeNode(0, n-1)
        root.init(0, n-1)
        for l, r, h in sorted(buildings, key=lambda b: b[2]):
            # Each tree node 'x' represents [x, x+1), so we need to track
            # [r-1, r) instead of [r, r+1).
            root.update_range(pos2idx[l], pos2idx[r]-1, h)

        ans = []
        def dfs(node):
            if node.a == node.b or node.lazy:
                if not ans or ans[-1][1] != node.val:
                    ans.append([idx2pos[node.a], node.val])
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return ans


class SegTreeNode:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.left = self.right = None
        self.lazy = False
        self.val = 0


    def init(self, a, b):
        if a == b:
            return

        m = (a + b) // 2
        if self.left is None:
            self.left = SegTreeNode(a, m)
            self.right = SegTreeNode(m+1, b)
        self.left.init(a, m)
        self.right.init(m+1, b)


    def update_range(self, a, b, val):
        if self.a > b or self.b < a:
            return

        if self.a == self.b:
            self.val = max(self.val, val)
            self.lazy = False
            return

        # Note we only use lazy update when the incoming val equal or greater
        if self.a >= a and self.b <= b and self.val <= val:
            self.val = val
            self.lazy = True
            return

        if self.lazy:
            self.left.val = self.right.val = self.val
            self.left.lazy = self.right.lazy = True
            self.lazy = False

        self.val = max(self.val, val)

        self.left.update_range(a, b, val)
        self.right.update_range(a, b, val)