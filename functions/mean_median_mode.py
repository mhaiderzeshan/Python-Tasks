"""
Create a function that takes a list of numbers and returns the mean, median and mode.
"""
from typing import List, Dict
from collections import defaultdict
import statistics


def mean_median_mode(numbers: List[int]):
    # calculate mean
    mean = sum(numbers) / len(numbers)

    # calculate median
    data = sorted(numbers)
    n = len(data)

    if n % 2 == 1:
        median = data[n // 2]
    else:
        mid_first = data[n // 2 - 1]
        mid_last = data[n // 2]
        median = (mid_first + mid_last) / 2

    # calculate mode
    freq: Dict[int, int] = defaultdict(int)
    for number in numbers:
        freq[number] += 1

    mode = max(freq.keys(), key=lambda k: freq[k])

    return mean, median, mode


numbers = [2, 5, 10, 4, 1, 2]
mean, median, mode = mean_median_mode(numbers)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
