# 406. Queue Reconstruction by Height
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        '''
        Sort people by height (reversely) and k.

        Highest people come first, among the highest people, the ones with
        smallest k come first. This way, when we look at a person (h, k), all
        existing people in the queue have equal or greater heights, and k would
        be the position of this new person.

        Time: O(n^2) where n is len(people)
        Space: O(n)
        '''
        people.sort(key=lambda p: (-p[0], p[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue