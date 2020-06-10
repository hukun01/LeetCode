# 406. Queue Reconstruction by Height
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        '''
        Sort people by height (reversely) and k.
        Highest people come first, among the highest people, the ones with smallest
        k come first.
        The highest persons' positions in the queue are just their k's, because
        only the other equal-height persons can affect these person's position.
        The second highest persons' positions are affected by the first group above,
        but not vice versa, so their positions are just their k's as well.
        '''
        people.sort(key=lambda p: (-p[0], p[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue