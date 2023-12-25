"""Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # create an empty hash set
        hash_set: set[int] = set()

        # for each num
        for num in nums:
            # if num is present in hash_set
            if num in hash_set:
                # return True
                return True

            # otherwise add num to hash_set
            hash_set.add(num)

        # at last return False
        return False


"""
Time complexity: O(n)
Space complexity: O(n)
"""
