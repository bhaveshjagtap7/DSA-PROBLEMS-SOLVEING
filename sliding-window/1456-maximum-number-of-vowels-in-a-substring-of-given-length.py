"""
LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length

Problem Statement:
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 has 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

def maxVowelsBruteForce(s: str, k: int) -> int:
    """
    Brute Force Approach:
    Iterate over every possible window of size k, count the number of vowels in each window,
    and keep track of the maximum count found.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_count = 0
    n = len(s)
    
    for i in range(n - k + 1):
        current_count = 0
        for j in range(i, i + k):
            if s[j] in vowels:
                current_count += 1
        max_count = max(max_count, current_count)
    
    return max_count
