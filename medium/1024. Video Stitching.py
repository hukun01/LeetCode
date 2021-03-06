# 1024. Video Stitching
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        '''
        1/2 Sorting
        Keep track of an interval [begin, end], in which 'furthest_end' tracks
        the largest distance we can reach from the *reachable, *continuous
        clips intervals that starts on or before 'cur_end'.

        From 'furthest_end' we start our next exploration in the continuous clips.

        We pick the furthest_end every time, the number of picks is the minimum
        number of clips that can stitch together to cover [0, T].

        Similar to 45. Jump Game II
        '''
        i = ans = furthest_end = cur_end = 0
        clips.sort()
        while cur_end < T:
            while i < len(clips) and clips[i][0] <= cur_end:
                furthest_end = max(furthest_end, clips[i][1])
                i += 1
            if furthest_end == cur_end:
                # we are not advancing, can't stitch up to T.
                return -1
            cur_end = furthest_end
            ans += 1
        return ans
        '''
        2/2 No sort(), but use bucket sort.
        We only pick the largest end for each start, and within the current end,
        we can pick the clip that takes us to the furthest_end.
        Only after that we need to pick a new clip.
        This solution relies on the fact that T is relatively small, because we
        need O(T) space and O(max(N, T)) time.
        '''
        ends = [0] * (T + 1)
        for s, e in clips:
            if s <= T:
                ends[s] = max(ends[s], min(e, T))
        i = ans = furthest_end = cur_end = 0
        while cur_end < T:
            while i <= cur_end:
                furthest_end = max(furthest_end, ends[i])
                i += 1
            if furthest_end == cur_end:
                return -1
            cur_end = furthest_end
            ans += 1
        return ans