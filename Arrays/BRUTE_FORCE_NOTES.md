# Brute Force Approach - Binary Search Problem

## Problem: Leetcode 704 Binary Search

### Brute Force Solution
**Approach**: Linear Search (Brute Force)
- Iterate through each element in the array sequentially
- Compare each element with the target
- Return index if found, otherwise return -1

### Code
```python
class Solution(object):
    def search(self, nums, target):
        # Brute Force: Linear Search
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```

### Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Why it's inefficient**: Must check every element even if array is sorted

### When to use Brute Force
- Small datasets (n < 1000)
- Unsorted arrays (cannot use binary search)
- When simplicity is prioritized over performance
