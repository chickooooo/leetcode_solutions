"""Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase,
typically using all the original letters exactly once.
"""


from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if unequal length
        if len(s) != len(t):
            # return False
            return False

        # create an empty hash map with default value as 0
        hash_map = defaultdict(int)

        # for each s_letter and t_letter
        for s_letter, t_letter in zip(s, t):
            # increment s_letter count
            hash_map[s_letter] += 1
            # decrement t_letter count
            hash_map[t_letter] -= 1

            # if s_letter count is 0
            if hash_map[s_letter] == 0:
                # delete s_letter key
                del hash_map[s_letter]
            # if t_letter count is 0
            if hash_map[t_letter] == 0:
                # delete t_letter key
                del hash_map[t_letter]

        # check if hash_map is empty
        return hash_map == {}


"""
Time complexity: O(n)
Space complexity: O(n)
"""
