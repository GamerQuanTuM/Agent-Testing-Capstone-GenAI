"""
Binary Search
Given a sorted array of integers and a target, return the index of target if present, otherwise -1.
This file intentionally contains a deliberate mistake (see comment).
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            # DELIBERATE MISTAKE: Wrong update — should be `left = mid + 1`
            # Here we incorrectly update `right` instead of `left`.
            right = mid + 1
        else:
            left = mid - 1
    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    print('binary_search 7 ->', binary_search(arr, 7))  # expected 3 but will be wrong due to the deliberate bug
