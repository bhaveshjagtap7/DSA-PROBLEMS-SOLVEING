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
        
        Interview Notes:
        ----------------
        KEY INSIGHT: Instead of asking "Does nums[j] exist where nums[i] + nums[j] = target?",
                     ask "Have I already seen (target - nums[i])?"
        
        This transforms O(n²) nested loops into O(n) single pass with hash map.
        
        APPROACH PROGRESSION (What to say in interview):
        1. Brute Force: Try all pairs → O(n²) time, O(1) space
        2. Optimized: Use hash map → O(n) time, O(n) space ✓
        
        COMMON MISTAKES TO AVOID:
        - Using same element twice (use i and j, not two pointers on sorted)
        - Returning values instead of indices
        - Not considering negative numbers
        - Forgetting there's exactly one solution (no need to check all)
        
        FOLLOW-UP QUESTIONS TO EXPECT:
        Q: What if array is sorted?
          A: Could use two pointers, but hash map is still O(n) and simpler
        
        Q: What if we need all pairs instead of one?
          A: Continue iterating instead of early return
        
        Q: What about space optimization?
          A: O(n) space is acceptable, brute force O(n²) time is too slow
        
        Q: What if we can't use extra space?
          A: Only option is O(n²) brute force
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


# ============================================================================
# INTERVIEW KEY OBSERVATIONS
# ============================================================================
"""
🎯 KEY OBSERVATIONS FOR INTERVIEWS:

1. PATTERN RECOGNITION
   - Classic "complement search" problem
   - Hash map for O(1) lookup is the key insight
   - Trade space for time: O(n) space saves O(n²) to O(n) time

2. WHY HASH MAP WORKS
   - For each element x, we need to find (target - x)
   - Instead of scanning rest of array O(n), use hash map O(1)
   - Store elements as we go, so we find pairs naturally

3. WHY NOT TWO POINTERS?
   - Two pointers require SORTED array
   - Sorting loses original indices
   - Problem asks for ORIGINAL indices
   - Sorting is O(n log n), worse than hash map O(n)

4. COMPLEXITY TRADE-OFF
   Time    Space   Approach
   ────────────────────────────
   O(n²)   O(1)    Brute force (too slow) ✗
   O(n)    O(n)    Hash map (optimal) ✓
   
5. EDGE CASES HANDLED
   ✓ Negative numbers (hash map works with any integer)
   ✓ Duplicates with different indices (use i and seen[remaining])
   ✓ Target is zero (e.g., -3 + 3 = 0)
   ✓ Minimum size array [x, y]

6. INTERVIEW TALKING POINTS
   - "I'll start with brute force O(n²) to show understanding"
   - "Can optimize using hash map to cache seen numbers"
   - "This is space-time tradeoff worth making"
   - "Hash map lookup is O(1) average case"
   - "Single pass algorithm, very efficient"

7. WHAT MAKES THIS PROBLEM "EASY"?
   - Clear problem statement
   - Guaranteed exactly one solution
   - Standard hash map pattern
   - No complex data structures
   - But still requires optimization thinking!

8. RELATED PATTERNS
   - 3Sum (extension of this)
   - 4Sum (further extension)
   - Two Sum II (sorted array variant)
   - Complement search pattern
"""
            
