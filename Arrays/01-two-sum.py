"""
LeetCode 1: Two Sum

Problem Statement:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Topic: Arrays + HashMap
Difficulty: Easy
"""

# ============================================================================
# OPTIMIZED APPROACH: HASH MAP (Single Pass)
# ============================================================================
"""
Strategy: Use a hash map to store numbers we've seen and their indices.
- Iterate through array once
- For each number, calculate what we need (target - current)
- Check if we've already seen that number
- If yes, return both indices
- If no, store current number and continue

Time Complexity: O(n) - Single pass through array
Space Complexity: O(n) - Hash map stores up to n elements

Why Hash Map?
- Lookup in hash map is O(1) average case
- Better than nested loops O(n²)
"""

# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
"""
Example: nums = [2, 7, 11, 15], target = 9

Initial state:
seen = {}

Iteration 1: i=0, nums[0]=2
  remaining = 9 - 2 = 7
  Is 7 in seen? No
  Add to seen: seen = {2: 0}

Iteration 2: i=1, nums[1]=7
  remaining = 9 - 7 = 2
  Is 2 in seen? Yes! (at index 0)
  Return [0, 1] ✓

Final Answer: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

---

Example 2: nums = [3, 2, 4], target = 6

Initial state:
seen = {}

Iteration 1: i=0, nums[0]=3
  remaining = 6 - 3 = 3
  Is 3 in seen? No
  Add to seen: seen = {3: 0}

Iteration 2: i=1, nums[1]=2
  remaining = 6 - 2 = 4
  Is 4 in seen? No
  Add to seen: seen = {3: 0, 2: 1}

Iteration 3: i=2, nums[2]=4
  remaining = 6 - 4 = 2
  Is 2 in seen? Yes! (at index 1)
  Return [1, 2] ✓

Final Answer: [1, 2]
Explanation: nums[1] + nums[2] = 2 + 4 = 6

---

Example 3: nums = [3, 3], target = 6

Initial state:
seen = {}

Iteration 1: i=0, nums[0]=3
  remaining = 6 - 3 = 3
  Is 3 in seen? No
  Add to seen: seen = {3: 0}

Iteration 2: i=1, nums[1]=3
  remaining = 6 - 3 = 3
  Is 3 in seen? Yes! (at index 0)
  Return [0, 1] ✓

Final Answer: [0, 1]
Explanation: nums[0] + nums[1] = 3 + 3 = 6
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        Find two numbers that add up to target.
        
        Args:
            nums: List of integers
            target: Target sum
        
        Returns:
            List of two indices [i, j] where nums[i] + nums[j] = target
        """
        # Hash map to store {number: index}
        seen = {}
        
        # Iterate through array
        for i in range(len(nums)):
            # Calculate what number we need to reach target
            remaining = target - nums[i]
            
            # Check if we've seen the complement
            if remaining in seen:
                return [seen[remaining], i]
            
            # Store current number and its index
            seen[nums[i]] = i
            
