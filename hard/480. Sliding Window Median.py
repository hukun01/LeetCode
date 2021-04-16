# 480. Sliding Window Median
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        '''
        Two heaps with lazy deletion.

        Similar to 295. Find Median from Data Stream, use two heaps to store
        the two small and large parts of the data.
        In this problem, we also need to move things out as numbers fall out
        of sliding window. Directly removing things from heaps are not
        efficient, so we do lazy deletions - deleting an element only when it
        becomes the top of the heaps. In the meantime, keep two heaps balanced.
        We can do lazy deletions because the median is impacted only by the
        heap tops, so we just need to ensure heap tops are valid.

        In the heap, store both the value and the index, the index is used to
        determine whether the entry is out of the window. Also, since Python
        provides min heap, we take the smaller index first, if there are
        duplicate values.

        Throughout the process, we keep two invariants to balance heaps:
        1. len(small) <= len(large) <= len(small) + 1
        2. -small[0][0] <= large[0][0]

        Pre-populate small and large heaps with nums[:k], then start using
        nums[k:] with non-empty heaps. 

        As we process nums[k:], we need to re-balance after using each element.
        Focus on balancing one heap, here we choose 'large'. If one heap is
        balanced, another is automatically balanced. Here balance means when
        the heap gets an element, it should lost one.

        Note that the balance is measured using the effective numbers in
        window, not the total numbers in heaps.

        To determine whether to add the current element 'x' to large, compare
        'x' with large[0][0]:
        1. if x >= large[0][0], we should add x to large.
            Once we add x to large, check the out-of-window element nums[i-k],
            if nums[i-k] < large[0][0], it means the nums[i-k] is in small,
            due to the variant #1.
            Since we just added to large and are going to remove from small,
            move one effective element (large[0]) from large to small, to keep
            balance.
            We also do above re-balance if nums[i-k] == large[0][0], because
            it covers the case that small[0][0] == large[0][0] and
            large[0][0] is older (smaller index due to initialization). And
            even if small[0][0] != large[0][0], moving doesn't hurt.

            If the nums[i-k] > large[0][0], we don't move large[0], because it
            is not valid to move to small, and we will get to large[0] later
            via lazy deletion.

        2. else, add x to small, and do similar movement.

        Then check the heap top and pop out outdated elements per indices.
        
        Time: O(n log(n)) where n is len(nums), as we do lazy deletion, we can
              have O(n) elements in the heaps.
        Space: O(n)
        '''
        small, large = [], []
        for i, a in enumerate(nums[:k]):
            heappush(small, (-a, i))

        def move(h1, h2):
            a, i = heappop(h1)
            heappush(h2, (-a, i))

        # If k is odd, 'large' has one more element.
        for _ in range(k - (k // 2)):
            move(small, large)

        def get_med():
            return large[0][0] if k & 1 else (large[0][0] - small[0][0]) / 2

        def lazy_delete(h):
            while h and h[0][1] <= i-k:
                heappop(h)

        ans = [get_med()]
        for i, a in enumerate(nums[k:], start=k):
            cur_med = ans[-1]
            if a >= cur_med:
                heappush(large, (a, i))
                if nums[i-k] <= cur_med:
                    move(large, small)
            else:
                heappush(small, (-a, i))
                if nums[i-k] >= cur_med:
                    move(small, large)

            lazy_delete(small)
            lazy_delete(large)

            ans.append(get_med())

        return ans