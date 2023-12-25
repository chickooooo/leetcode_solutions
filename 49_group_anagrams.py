"""Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by
rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # create empty hash map with default value as []
        hash_map = defaultdict(list)

        # for each word
        for word in strs:
            # sort the word and create the key
            key = "".join(sorted(word))
            # append the word using the key in the hash map
            hash_map[key].append(word)

        # return list of hash map values
        return list(hash_map.values())


"""
Time complexity: O(n)
Space complexity: O(n)
"""
