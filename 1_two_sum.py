"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # create an empty hash map
        hash_map = {}

        # for each num
        for i, num in enumerate(nums):
            # find it's twin
            twin = target - num

            # if twin is present in hash_map
            if twin in hash_map:
                # return num's index and twin's index
                return [i, hash_map[twin]]

            # otherwise add num & it's index to hashmap
            hash_map[num] = i

        # if not found, return empty array
        return []


"""
Time complexity: O(n)
Space complexity: O(n)
"""
