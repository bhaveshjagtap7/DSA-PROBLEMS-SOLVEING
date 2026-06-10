"""
LeetCode 49: Group Anagrams

Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

from collections import defaultdict

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def is_anagram(str1: str, str2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    Two strings are anagrams if their sorted representations are identical.
    """
    return sorted(str1) == sorted(str2)


# ============================================================================
# APPROACH 1: INITIAL/BRUTE FORCE GROUPING
# ============================================================================

def groupAnagrams_initial(strs):
    """
    Initial grouping approach.
    We iterate through the input strings. For each string, we try to place it
    into an existing group of anagrams. We determine if a string belongs to a group
    by comparing its sorted character list with the sorted version of the first
    string in the group.
    
    If it fits in an existing group, we append it. Otherwise, we create a new group.
    """
    groups = []
    
    for s in strs:
        found_group = False
        for group in groups:
            # Check if current string is an anagram of the group representative
            if is_anagram(s, group[0]):
                group.append(s)
                found_group = True
                break
        
        # If no matching group is found, create a new group
        if not found_group:
            groups.append([s])
            
    return groups


# ============================================================================
# APPROACH 2: HASHMAP OPTIMIZATION (Sorted String Key)
# ============================================================================

def groupAnagrams_hashmap(strs):
    """
    HashMap-based approach.
    Key insight: All anagrams will yield the exact same string when sorted.
    By using the sorted string as a key in a hash map, we can group all anagrams
    together in O(N * K log K) time, where N is the number of strings and K is the
    maximum length of a string.
    """
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Sort the characters of s and join them back into a string key
        sorted_key = "".join(sorted(s))
        # Group s under this unique sorted key
        anagram_map[sorted_key].append(s)
        
    return list(anagram_map.values())


# ============================================================================
# APPROACH 3: OPTIMIZED HASHMAP (Character Count Key)
# ============================================================================

def groupAnagrams_optimized(strs):
    """
    Optimized HashMap-based approach.
    Instead of sorting each string (which takes O(K log K) time), we compute the
    frequency of each character (a-z) in O(K) time.
    We use a tuple of size 26 containing these frequencies as the key in our map.
    This runs in O(N * K) time.
    """
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Create a frequency count array of size 26 for lowercase English letters
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
            
        # Convert list to tuple to make it hashable and use it as key
        anagram_map[tuple(count)].append(s)
        
    return list(anagram_map.values())
