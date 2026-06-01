# Binary Search - Complete Solution with Test Cases

## Problem Statement
Leetcode 704: Binary Search
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, return its index. Otherwise, return -1.

## Optimized Solution in Python

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Avoid potential overflow
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1
        
        # Target not found
        return -1
```

## Test Cases

```python
def test_binary_search():
    solution = Solution()
    
    # Test case 1: Target found at index
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    print("Test 1 passed: Target 9 found at index 4")
    
    # Test case 2: Target not in array
    assert solution.search([-1, 0, 3, 5, 9, 12], 13) == -1
    print("Test 2 passed: Target 13 not found, returned -1")
    
    # Test case 3: Target at beginning
    assert solution.search([-1, 0, 3, 5, 9, 12], -1) == 0
    print("Test 3 passed: Target -1 found at index 0")
    
    # Test case 4: Single element array - found
    assert solution.search([5], 5) == 0
    print("Test 4 passed: Single element found")
    
    # Test case 5: Single element array - not found
    assert solution.search([5], 3) == -1
    print("Test 5 passed: Single element not found")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_binary_search()
```

## Key Points
- Binary search works on **sorted arrays only**
- Always eliminates half of the remaining elements in each iteration
- Efficient approach for large datasets
