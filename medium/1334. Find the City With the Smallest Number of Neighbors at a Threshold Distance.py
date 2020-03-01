# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        '''
        Floyd-Warshall Algorithm. Iterate through all middle points k, to find the
        min distance bewteen i and j, by looking at each pair dis[i][k] and dis[k][j]
        that can form dis[i][j].
        '''
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, distance in edges:
            dis[i][j] = dis[j][i] = distance
            dis[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        count = float('inf')
        ans = 0
        for i in range(n):
            currCount = sum(dis[i][j] <= distanceThreshold and i != j for j in range(n))
            if currCount <= count:
                ans = i
                count = currCount
        return ans