class Solution:
    def lengthLongestPath(self, input: str) -> int:
        '''
        Need to know str.splitlines() instead of str.split('\n'), and str.lstrip()
        that return a copy of the string with leading characters removed.

        The major logic is to use a dict to store the { depth : pathLen }, and
        the depth is the number of tabs in each string piece.
        It's ok to override it as we just need to visit each piece once.
        '''
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen