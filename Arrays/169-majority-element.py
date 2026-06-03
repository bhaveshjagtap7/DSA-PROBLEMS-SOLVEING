"""
LeetCode 169: Majority Element

Problem Statement:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?

Difficulty: Easy
Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting
"""


# ============================================================================
# EXAMPLES
# ============================================================================
"""
Example 1:
Input: nums = [3, 2, 3]
Output: 3
Explanation: 3 appears 2 times, which is more than ⌊3/2⌋ = 1

Example 2:
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
Explanation: 2 appears 4 times, which is more than ⌊7/2⌋ = 3

Example 3:
Input: nums = [1]
Output: 1
Explanation: 1 appears 1 time, which is more than ⌊1/2⌋ = 0

Example 4:
Input: nums = [6, 5, 5]
Output: 5
Explanation: 5 appears 2 times, which is more than ⌊3/2⌋ = 1

Example 5:
Input: nums = [10, 9, 9, 9, 10]
Output: 9
Explanation: 9 appears 3 times, which is more than ⌊5/2⌋ = 2
"""



# ============================================================================
# APPROACH 1: BRUTE FORCE
# ============================================================================
"""
Strategy: Count occurrences of each element using nested loops.
For each element, count how many times it appears in the array.
If count > n/2, return that element.

Time Complexity: O(n²) - Nested loops
Space Complexity: O(1) - No extra space used
"""

def majorityElement_bruteforce(nums):
    """
    Brute force approach with nested loops.
    
    Args:
        nums: List of integers
    
    Returns:
        The majority element (appears more than n/2 times)
    """
    array_length = len(nums)
    majority_threshold = array_length // 2
    
    # Check each element
    for current_element in nums:
        occurrence_count = 0
        
        # Count how many times current element appears
        for element in nums:
            if element == current_element:
                occurrence_count += 1
        
        # If count exceeds threshold, we found majority element
        if occurrence_count > majority_threshold:
            return current_element



# ============================================================================
# APPROACH 2: HASH MAP (Better Approach)
# ============================================================================
"""
Strategy: Use hash map to count frequency of each element in single pass.
Store counts in dictionary, then find element with count > n/2.

Time Complexity: O(n) - Single pass through array
Space Complexity: O(n) - Hash map stores up to n unique elements
"""

def majorityElement_hashmap(nums):
    """
    Hash map approach for counting element frequencies.
    
    Args:
        nums: List of integers
    
    Returns:
        The majority element (appears more than n/2 times)
    """
    array_length = len(nums)
    majority_threshold = array_length // 2
    
    # Dictionary to store element frequencies
    frequency_map = {}
    
    # Count frequency of each element
    for element in nums:
        frequency_map[element] = frequency_map.get(element, 0) + 1
        
        # Early exit: if we found majority element, return immediately
        if frequency_map[element] > majority_threshold:
            return element



# ============================================================================
# COMPLEXITY ANALYSIS
# ============================================================================
"""
APPROACH COMPARISON:

Approach              Time         Space        Notes
─────────────────────────────────────────────────────────────────
Brute Force          O(n²)        O(1)         Simple, too slow
Hash Map             O(n)         O(n)         Good, but uses space
Sorting              O(n log n)   O(1)*        *Modifies array
Boyer-Moore          O(n)         O(1)         Optimal! ✓

WHY BOYER-MOORE IS OPTIMAL:
- Linear time O(n): Single pass through array
- Constant space O(1): Only two variables (candidate + count)
- No sorting needed: Works on unsorted array
- No extra memory: No hash map or additional data structures
- Elegant algorithm: Based on voting/cancellation concept

SCALABILITY:
For n = 1,000,000 elements:
- Brute Force:   ~500 billion operations (O(n²))
- Hash Map:      ~1 million operations (O(n)) + hash map memory
- Sorting:       ~20 million operations (O(n log n))
- Boyer-Moore:   ~1 million operations (O(n)) + minimal memory ✓

RECOMMENDATION: Use Boyer-Moore for optimal solution!
"""



# ============================================================================
# APPROACH 3: BOYER-MOORE VOTING ALGORITHM (Optimal)
# ============================================================================
"""
Strategy: Voting algorithm based on majority element cancellation.

Key Insight:
- If we cancel out each occurrence of majority element with different element,
  the majority element will still remain at the end.
- Majority element appears MORE than n/2 times, so it survives cancellation.

Algorithm:
1. Initialize candidate = None, count = 0
2. For each element:
   - If count == 0, set current element as new candidate
   - If element == candidate, increment count
   - If element != candidate, decrement count
3. Return candidate (guaranteed to be majority element)

Why it works:
- When count reaches 0, we've cancelled equal numbers of different elements
- Majority element appears more than all others combined
- So majority element will always be the final candidate

Time Complexity: O(n) - Single pass through array
Space Complexity: O(1) - Only two variables used
"""

def majorityElement_boyer_moore(nums):
    """
    Boyer-Moore Voting Algorithm (Optimal Solution).
    
    Args:
        nums: List of integers
    
    Returns:
        The majority element (appears more than n/2 times)
    """
    # Initialize candidate and vote count
    candidate = None
    vote_count = 0
    
    # Find candidate using voting algorithm
    for current_element in nums:
        # If count is 0, elect new candidate
        if vote_count == 0:
            candidate = current_element
            vote_count = 1
        # If current element matches candidate, increase vote
        elif current_element == candidate:
            vote_count += 1
        # If current element differs, decrease vote (cancellation)
        else:
            vote_count -= 1
    
    # Candidate is guaranteed to be majority element (per problem constraints)
    return candidate


class Solution(object):
    """LeetCode 169: Majority Element Solution"""
    
    def majorityElement(self, nums):
        """
        Find the majority element using Boyer-Moore Voting Algorithm.
        
        Args:
            nums: List of integers
        
        Returns:
            The majority element
        """
        return majorityElement_boyer_moore(nums)



# ============================================================================
# DRY RUN: BOYER-MOORE VOTING ALGORITHM
# ============================================================================
"""
DRY RUN 1: nums = [2, 2, 1, 1, 1, 2, 2]

Initial state:
candidate = None, vote_count = 0

Iteration 1: element = 2
  vote_count == 0? YES → Elect new candidate
  candidate = 2, vote_count = 1

Iteration 2: element = 2
  element == candidate? YES → Increase vote
  vote_count = 2

Iteration 3: element = 1
  element == candidate? NO → Decrease vote (cancellation)
  vote_count = 1

Iteration 4: element = 1
  element == candidate? NO → Decrease vote
  vote_count = 0

Iteration 5: element = 1
  vote_count == 0? YES → Elect new candidate
  candidate = 1, vote_count = 1

Iteration 6: element = 2
  element == candidate? NO → Decrease vote
  vote_count = 0

Iteration 7: element = 2
  vote_count == 0? YES → Elect new candidate
  candidate = 2, vote_count = 1

Final Answer: candidate = 2 ✓
(2 appears 4 times, which is > 7/2 = 3.5)

---

DRY RUN 2: nums = [3, 2, 3]

Initial state:
candidate = None, vote_count = 0

Iteration 1: element = 3
  vote_count == 0? YES → Elect new candidate
  candidate = 3, vote_count = 1

Iteration 2: element = 2
  element == candidate? NO → Decrease vote
  vote_count = 0

Iteration 3: element = 3
  vote_count == 0? YES → Elect new candidate
  candidate = 3, vote_count = 1

Final Answer: candidate = 3 ✓
(3 appears 2 times, which is > 3/2 = 1.5)

---

DRY RUN 3: nums = [1]

Initial state:
candidate = None, vote_count = 0

Iteration 1: element = 1
  vote_count == 0? YES → Elect new candidate
  candidate = 1, vote_count = 1

Final Answer: candidate = 1 ✓
(1 appears 1 time, which is > 1/2 = 0.5)

---

KEY OBSERVATION:
The voting/cancellation mechanism ensures that the majority element
survives because it appears MORE than all other elements COMBINED.
Even if every occurrence of majority element is paired with a different
element for cancellation, there will still be majority elements remaining.
"""



# ============================================================================
# EDGE CASES
# ============================================================================
"""
Edge Cases to Consider:

1. Single element array [x]
   → x is majority element (appears 1 time > 1/2 = 0.5)

2. Two elements, same [x, x]
   → x is majority element

3. Two elements, different [x, y]
   → One must be majority (problem guarantees majority exists)

4. All elements are same [x, x, x, x, ...]
   → x is majority element

5. Majority element at start [x, x, x, y, z]
   → Algorithm handles correctly

6. Majority element at end [y, z, x, x, x]
   → Algorithm handles correctly

7. Majority element scattered [x, y, x, z, x]
   → Algorithm handles correctly

8. Negative numbers [-1, -1, 2]
   → Works with any integers

9. Large numbers within constraints
   → Algorithm is value-agnostic

10. Array length at boundary (1 or 50,000)
    → Algorithm scales linearly

IMPORTANT NOTE:
The problem GUARANTEES that majority element always exists.
We don't need to verify if candidate is actually majority element.
The Boyer-Moore algorithm will always return correct answer when majority exists.

If verification was needed (not for this problem):
- Do second pass to count candidate occurrences
- Check if count > n/2
- This would still be O(n) time
"""
