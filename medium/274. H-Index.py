class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        1/2 Sort.
        Imagine plotting a histogram where the y-axis represents
        the number of citations for each paper.
        After sorting in descending order, h-index is the length
        of the largest square in the histogram.
        '''
        return sum(citation > idx for idx, citation in 
                   enumerate(sorted(citations, reverse=True)))
        '''
        2/2 Counting sort.
        Since the h-index is upper bounded by the total
        number of citations 'n', for any citation
        greater than 'n', we can replace it with 'n'.

        Then from high to low, find the max index where
        the number of papers with at least this citation exceeds the citation.
        '''
        n = len(citations)
        citation_to_paper_count = [0] * (n + 1)
        for c in citations:
            citation_to_paper_count[min(n, c)] += 1
        count = 0
        for c in range(n, -1, -1):
            count += citation_to_paper_count[c]
            if count >= c:
                return c
        return 0