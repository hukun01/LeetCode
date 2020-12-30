# 388. Longest Absolute File Path
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        '''
        String.
        Prefer str.splitlines() than str.split('\n'), because the former
        doesn't keep the end, e.g., "xx\n".splitlines() returns ["xx"], while
        "xx\n".split('\n') returns ["xx", ""]
        Also, use str.lstrip() to return a copy of the string with leading
        characters removed.

        Also, remember to count the slashes between directories.

        The major logic is to use a dict to store the { depth : pathLen }, and
        the depth is the number of leading tabs in each string piece.
        It's ok to override it as we just need to visit each piece once.

        Time: O(n) where n is len(input)
        Space: O(d) where d is the max depth of the directories
        '''
        path_lens = Counter()
        ans = 0
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                ans = max(ans, path_lens[depth-1] + len(name))
            else:
                path_lens[depth] = path_lens[depth-1] + len(name) + 1
        return ans