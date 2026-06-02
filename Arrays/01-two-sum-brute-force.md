# Two Sum - Brute Force Approach

## Strategy
Compare every pair of numbers to find two that sum to target.

## Algorithm
```
For each element at index i:
    For each element at index j (where j > i):
        If nums[i] + nums[j] == target:
            Return [i, j]
```

## Complexity
- **Time:** O(n²) - Two nested loops
- **Space:** O(1) - No extra space needed

## Python Implementation
```python
def twoSum_bruteforce(nums, target):
    """Brute force with nested loops."""
    n = len(nums)
    
    # Check every pair
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []  # No solution found
```

## Dry Run Example
**Input:** nums = [2, 7, 11, 15], target = 9

```
i=0, nums[0]=2:
  j=1, nums[1]=7:  2 + 7 = 9 ✓ MATCH!
  Return [0, 1]
```

**Input:** nums = [3, 2, 4], target = 6

```
i=0, nums[0]=3:
  j=1, nums[1]=2:  3 + 2 = 5 ✗
  j=2, nums[2]=4:  3 + 4 = 7 ✗

i=1, nums[1]=2:
  j=2, nums[2]=4:  2 + 4 = 6 ✓ MATCH!
  Return [1, 2]
```

## Why Not Optimal?
- For 1000 elements: ~500,000 comparisons
- For 10,000 elements: ~50 million comparisons
- Gets very slow for large inputs

## Better Approach
Use **Hash Map** → O(n) time, O(n) space
