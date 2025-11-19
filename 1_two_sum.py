"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""
from typing import List, Optional

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """Return indices of the two numbers adding up to target.

    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("two_sum:", two_sum(nums, target))  # expected [0,1]
