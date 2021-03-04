from collections import *
from itertools import *
from random import *
import sys
import time
from typing import List

def generate_k_random_unique_within_n(k, n):
    data = list(range(n))
    for i in range(k):
        j = randrange(i, n)
        data[i], data[j] = data[j], data[i]
        yield data[i]

if __name__ == "__main__":
    print(list(generate_k_random_unique_within_n(5, 10)))