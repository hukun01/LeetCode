# 1345. Jump Game IV
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        '''
        The key is to exclude the visited indicies and values, to avoid 反复横跳.
        1/2 Two end BFS.
        '''
        val_to_idx = collections.defaultdict(list)
        for i, a in enumerate(arr):
            val_to_idx[a].append(i)
 
        begins = set([0])
        ends = set([len(arr) - 1])
        visited_idx = set([-1, len(arr)])
        for steps in range(len(arr)):
            if len(begins) > len(ends):
                begins, ends = ends, begins
            next_level = set()
            for b in begins:
                if b in ends:
                    return steps
                if b in visited_idx:
                    continue
                visited_idx.add(b)
                next_level.update([b - 1, b + 1] + val_to_idx[arr[b]])
                val_to_idx.pop(arr[b]) # this is the key
            begins = next_level

        '''
        2/2 Regular BFS.
        '''
        val_to_idx = collections.defaultdict(list)
        for i, a in enumerate(arr):
            val_to_idx[a].append(i)

        visited_idx = set([-1, len(arr)])
        q = collections.deque([(0, 0)])
        while q:
            step, pos = q.popleft()
            if pos == len(arr) - 1:
                return step
            for p in [pos - 1, pos + 1] + val_to_idx[arr[pos]]:
                if p not in visited_idx:
                    visited_idx.add(p)
                    q.append((step + 1, p))
            val_to_idx.pop(arr[pos]) # this is the key