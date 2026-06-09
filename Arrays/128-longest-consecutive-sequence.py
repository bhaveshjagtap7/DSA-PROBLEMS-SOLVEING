"""
Problem Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Initial Approach Discussion:
The naive approach is to sort the array and then find the longest consecutive streak.
Sorting takes O(n log n) time.

HashSet based optimization:
To achieve O(n) time, we can use a HashSet. By storing all numbers in a HashSet, we can do O(1) lookups.

Final O(n) solution:
We only start counting a sequence if `num - 1` is not in the set.
This ensures we only start from the beginning of a sequence.

Complexity analysis:
- Time Complexity: O(n). Although there is a nested loop, the inner loop only runs for the length of each consecutive sequence. Each number is visited at most twice.
- Space Complexity: O(n). We use a HashSet to store all numbers.

Edge cases:
- Empty array: returns 0
- Array with duplicates: HashSet automatically handles duplicates
- All elements consecutive: handled efficiently in one inner loop run

Dry run:
nums = [100, 4, 200, 1, 3, 2]
1. num_set = {1, 2, 3, 4, 100, 200}
2. num = 100. 99 not in set. current_num = 100, current_streak = 1. longest_streak = 1.
3. num = 4. 3 in set. Skip.
4. num = 200. 199 not in set. current_num = 200, current_streak = 1. longest_streak = 1.
5. num = 1. 0 not in set. current_num = 1. Loop 2, 3, 4. current_streak = 4. longest_streak = 4.

Interview insights:
- Always clarify if the array can be empty or have duplicates.
- The trick to achieving O(n) is the `if num - 1 not in num_set` condition.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence.
        """
        # Edge case: empty list
        if not nums:
            return 0
            
        # Create a HashSet for O(1) lookups
        num_set = set(nums)
        longest_sequence_length = 0
        
        for number in num_set:
            # Check if it is the start of a sequence
            if number - 1 not in num_set:
                current_number = number
                current_sequence_length = 1
                
                # Expand the sequence
                while current_number + 1 in num_set:
                    current_number += 1
                    current_sequence_length += 1
                    
                # Update the maximum sequence length
                longest_sequence_length = max(longest_sequence_length, current_sequence_length)
                
        return longest_sequence_length
