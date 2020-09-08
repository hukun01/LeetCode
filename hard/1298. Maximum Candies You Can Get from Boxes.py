# 1298. Maximum Candies You Can Get from Boxes
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        '''
        BFS.
        Maintain a seen_boxes that tracks the boxes we have seen but not
        necessarily the ones we can open.
        Maintain a visiting list of boxes that we can open, add contained
        boxes to visiting if they are opened. Always add them to seen_boxes.
        For each new box that can be opened with new keys, if the status
        is closed, and we have seen it, we add it to the visiting, as we
        can open it. For each box with new key, we set its status to be open,
        so next time if we see it in the contained boxes, we will visit it.
        '''
        seen_boxes = set(initialBoxes)
        visiting = [b for b in initialBoxes if status[b] == 1]
        for box in visiting:
            for cb in containedBoxes[box]:
                seen_boxes.add(cb)
                if status[cb] == 1:
                    visiting.append(cb)
            for kb in keys[box]:
                if status[kb] == 0 and kb in seen_boxes:
                    visiting.append(kb)
                status[kb] = 1
        return sum(candies[i] for i in visiting)