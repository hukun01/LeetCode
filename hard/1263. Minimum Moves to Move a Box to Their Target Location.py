# 1263. Minimum Moves to Move a Box to Their Target Location
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        '''
        Dijkstra.

        A trick is that if the box can be pushed, then the player's next
        position would be the box's current position, and vice versa.
        '''
        R, C = len(grid), len(grid[0])
        pos = {
            grid[r][c]: (r, c)
            for r in range(R)
            for c in range(C)
            if grid[r][c] in 'SBT'
        }

        box_pos = pos['B']
        player_pos = pos['S']
        target_pos = pos['T']

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(0, box_pos, player_pos)] # (push, box_pos, player_pos)
        visited = set()

        def inbound(r, c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] != '#'

        while pq:
            push, box_pos, player_pos = heappop(pq)
            if box_pos == target_pos:
                return push

            if (box_pos, player_pos) in visited:
                continue
            visited.add((box_pos, player_pos))
            br0, bc0 = box_pos
            pr0, pc0 = player_pos
            for dr, dc in dirs:
                pr1, pc1 = dr + pr0, dc + pc0
                br1, bc1 = dr + br0, dc + bc0
                if inbound(pr1, pc1):
                    if (pr1, pc1) == box_pos:
                        if inbound(br1, bc1):
                            heappush(pq, (push + 1, (br1, bc1), (pr1, pc1)))
                    else:
                        heappush(pq, (push, box_pos, (pr1, pc1)))

        return -1