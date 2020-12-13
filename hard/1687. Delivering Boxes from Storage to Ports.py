# 1687. Delivering Boxes from Storage to Ports
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        '''
        DP + sliding window minimum.
        Boxes can only be moved sequentially, this implies a DP solution.
        Let f[i] be the answer for handling boxes[:i], and moves[i] be the
        number of moves between ports, aka, the number of differences between
        the ports of consecutive boxes within boxes[:i]. Now we have
        f[i] = min(f[j] + moves[i] - moves[j+1] + 2
            for all j within box count and weight limit)
        In above equation, f[j] + (moves[i] - moves[j+1] + 2) is answer to move
        boxes[:j] (cost f[j]) and boxes[j+1:i] (the rest). Note that the moves
        in boxes[j+1:i] is (moves[i] - moves[j+1]) not (moves[i] - moves[j]).

        Time is O(n^2), not good enough. Note that above equation can be
        tranformed to f[j] - moves[j+1] + moves[i] + 2.
        Let g[j] = f[j] - moves[j+1], given i, box count and weight are
        increasing as j moves to right. If j0 violates count or weight
        constraint, we have to move j0 to the right, and moving i doesn't
        help. This implies a sliding window solution that helps find min(g[j])
        in O(1) time. We keep track of all g[j] based on all seen f[i], and
        pop out g[j] that expires due to box count and weight constraints.

        Time: O(n)
        Space: O(n)

        Similar to hacker_cup/2020/qualification/q4.py.
        '''
        n = len(boxes)
        W = [0] + list(accumulate(b[1] for b in boxes))
        moves = [0, 0] + list(accumulate(
            int(b1[0] != b2[0]) for b1, b2 in zip(boxes, boxes[1:])))
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        min_g_idxs = deque([0])
        for i in range(1, n+1):
            while i - (j := min_g_idxs[0]) > maxBoxes or W[i] - W[j] > maxWeight:
                min_g_idxs.popleft()
            f[i] = g[j] + moves[i] + 2
            if i < n:
                g[i] = f[i] - moves[i + 1]
                while g[i] <= g[min_g_idxs[-1]]:
                    min_g_idxs.pop()
                min_g_idxs.append(i)

        return f[-1]