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
