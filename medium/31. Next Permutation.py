class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ 1. Traverse the given number from rightmost digit, 
        keep traversing till you find a digit which is smaller than the previously traversed digit. 
        For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. 
        If we do not find such a digit, then output is “Not Possible”.
        2. Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. 
        For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.
        3. Swap the above found two digits, we get 536974 in above example.
        4. Now sort all digits from position next to ‘d’ to the end of number. 
        The number that we get after sorting is the output. For above example, 
        we sort digits in bold 536974. We get “536479” which is the next greater number for input 534976.
        Because this part is monotonically increasing (reversely), we just need to reverse it.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            nums.sort()
            return
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = reversed(nums[i + 1 :])