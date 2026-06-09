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
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
