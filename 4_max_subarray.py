"""
Maximum Subarray (Kadane's algorithm)
Return the largest sum of a contiguous subarray.
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    if not nums:
        raise ValueError('nums must be non-empty')
    max_ending_here = nums[0]
    max_so_far = nums[0]
    for x in nums[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == '__main__':
    print('max_subarray [−2,1,−3,4,−1,2,1,−5,4] ->',
          max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected 6
