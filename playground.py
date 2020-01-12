import sys
class Solution:
    def solve(self):
        '''
        Given 3 bottles with size being 10, 7, 3. The first bottle is initially full.
        What's the shortest steps to split the water evenly into two bottles?
        '''
        init = (10, 0, 0)
        target = (5, 5, 0)
        def bfs():
            paths = [[(init)]]
            visited = set()
            while paths:
                newPaths = []
                for path in paths:
                    pos = path[-1]
                    if pos == target:
                        return path
                    visited.add(pos)
                    limits = [10, 7, 3]
                    for i in range(3):
                        if pos[i] > 0:
                            for j in range(3):
                                if i == j:
                                    continue
                                if pos[j] < limits[j]:
                                    water = min(pos[i], limits[j] - pos[j])
                                    l = [0, 0, 0]
                                    l[i] = pos[i] - water
                                    l[j] = pos[j] + water
                                    l[3 - i - j] = pos[3 - i - j]
                                    new = tuple(l)
                                    if new not in visited:
                                        clone = path[:]
                                        clone.append(new)
                                        newPaths.append(clone)
                paths = newPaths

        print(bfs())

if __name__ == "__main__":
    solution = Solution()
    solution.solve()