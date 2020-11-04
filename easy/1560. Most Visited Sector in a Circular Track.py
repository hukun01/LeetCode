# 1560. Most Visited Sector in a Circular Track
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        '''
        Brain teaser.
        Only think about the extra part of all rounds, no need to simulate.
        The extra part is defined by the start and end of total rounds.
        '''
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end+1))
        return list(range(1, end+1)) + list(range(start, n+1))