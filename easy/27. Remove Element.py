class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        The key is to write concise code/logic.
        Iterate through the array, if the current element is not val, write it in-place 
        to the array. After the iteration, the end index is the total count of numbers
        that are not equal to val.
        
        Time: O(n)
        Space: O(1)
        '''
        i = 0
        for a in nums:
            if a != val:
                nums[i] = a
                i += 1
        return i
