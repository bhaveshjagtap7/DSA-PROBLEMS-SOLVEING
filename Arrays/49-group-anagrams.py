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
            if sorted(s) == sorted(group[0]):
                group.append(s)
                found_group = True
                break
        
        # If no matching group is found, create a new group
        if not found_group:
            groups.append([s])
            
    return groups
