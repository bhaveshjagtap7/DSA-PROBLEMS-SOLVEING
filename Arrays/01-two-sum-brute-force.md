# LeetCode 1 - Two Sum | Brute Force Approach

## Problem
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target.

## Brute Force Solution
```python
class Solution:
    def twoSum(self, nums, target):
        # Brute Force: Check every pair
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

## Analysis
- **Time Complexity**: O(n²) - Two nested loops
- **Space Complexity**: O(1) - No extra space
- **Why inefficient**: Checks all pairs even if solution found early

## When to use
- Small arrays (n < 100)
- When simplicity matters more than speed
- Interview warm-up or sanity check

## Example Execution
```
nums = [2, 7, 11, 15], target = 9

i=0, j=1: 2 + 7 = 9 ✓ → return [0, 1]
```

## Optimization
Switch to **HashMap approach** for O(n) time complexity!
