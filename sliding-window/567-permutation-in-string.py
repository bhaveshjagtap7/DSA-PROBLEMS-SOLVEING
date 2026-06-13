"""
LeetCode 567 - Permutation in String

Problem Statement:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is a substring of s2.

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

"""
Initial Brute Force Idea:
1. Generate all permutations of s1 (O(n!))
2. Check each permutation to see if it exists as a substring of s2 (O(m * n))
Total time: O(n! * m * n) — this is way too slow for n >= 10, let alone 10^4!
So we definitely need a smarter approach!
"""

"""
Frequency Map Explanation:
Since two strings are permutations of each other if and only if they have exactly the same character frequencies,
we don't need to generate permutations at all! Instead, we can count the frequency of each character in s1,
and then check if any window of length len(s1) in s2 has the exact same frequency counts!
"""

# Helper to create frequency map for a string
def get_frequency_map(s: str) -> list[int]:
    freq = [0] * 26  # 26 lowercase English letters
    for char in s:
        freq[ord(char) - ord('a')] += 1
    return freq


"""
Sliding Window Intuition:
- We need to check all windows of length len(s1) in s2
- Instead of recalculating frequency map for each window from scratch,
  we can maintain a sliding frequency map that adds the new character entering the window
  and removes the character that's leaving the window (as we slide the window)
- When the sliding window's frequency matches s1's frequency, return True!
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        # If s1 is longer than s2, impossible to have permutation
        if len_s1 > len_s2:
            return False
        
        # Step 1: Get frequency map for s1
        s1_freq = get_frequency_map(s1)
        
        # Step 2: Initialize frequency map for initial window of s2 (first len_s1 characters)
        window_freq = get_frequency_map(s2[:len_s1])
        
        return False
