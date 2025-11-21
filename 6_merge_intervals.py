"""
Merge Intervals
Given a list of intervals where each interval is [start, end], merge all overlapping intervals and return the result.
"""
from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]
    for s, e in intervals[1:]:
        last = merged[-1]
        if s <= last[1]:
            # Overlap -> merge
            last[1] = max(last[1], e)
        else:
            merged.append([s, e])
    return merged


if __name__ == '__main__':
    examples = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([], []),
        ([[1,4],[0,2],[3,5]], [[0,5]])
    ]
    for inp, expected in examples:
        out = merge_intervals([iv[:] for iv in inp])
        print(f"merge_intervals({inp}) -> {out}  expected: {expected}")
