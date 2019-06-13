'''
Google Telephonic Coding Interview Question
We need to sort array A, array B contains indices to corresponding elements
in array A with their correct sorted location.

Requirements: Time O(n) with constant space
'''
from typing import List

A = [21, 41, 61, 11, 81]
B = [2, 3, 4, 1, 5]

def sortAWithB(A: List[int], B: List[int]) -> List[int]:
    idxInB = 0
    while idxInB < len(B):
        trueIdxInA = B[idxInB] - 1
        A[idxInB], A[trueIdxInA] = A[trueIdxInA], A[idxInB]
        B[idxInB], B[trueIdxInA] = B[trueIdxInA], B[idxInB]
        if B[idxInB] - 1 == idxInB:
            idxInB += 1
    return A

if __name__ == "__main__":
    print("A:",A)
    print("B:",B)
    print(sortAWithB(A, B))