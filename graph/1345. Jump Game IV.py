# 1345. Jump Game IV
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        '''
        The key is to exclude the visited indicies and values, to avoid 反复横跳.
        1/2 Two end BFS.
        '''
        maps = collections.defaultdict(list)
        [maps[a].append(i) for i, a in enumerate(arr)]
 
        begins = set([0])
        ends = set([len(arr) - 1])
        visitedIdx = set([-1, len(arr)])
        for steps in range(len(arr)):
            if len(begins) > len(ends):
                begins, ends = ends, begins
            nextLevels = set()
            for b in begins:
                if b in ends:
                    return steps
                if b in visitedIdx:
                    continue
                visitedIdx.add(b)
                nextLevels.update([b - 1, b + 1] + maps[arr[b]])
                maps.pop(arr[b])
            begins = nextLevels

        '''
        2/2 Regular BFS.
        '''
        maps = collections.defaultdict(list)
        [maps[a].append(i) for i, a in enumerate(arr)]
        
        visitedIdx = set([-1, len(arr)])
        q = collections.deque([(0, 0)])
        while q:
            step, pos = q.popleft()
            if pos == len(arr) - 1:
                return step
            for p in [pos - 1, pos + 1] + maps[arr[pos]]:
                if p not in visitedIdx:
                    visitedIdx.add(p)
                    q.append((step + 1, p))
            maps.pop(arr[pos])