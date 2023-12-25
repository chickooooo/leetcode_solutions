"""Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # hash set of nums
        hash_set = set(nums)
        # will hold max count
        max_count = 0

        # for each num
        for num in nums:
            # if num is start of a sequence
            if num - 1 not in hash_set:
                # set count to 0
                count = 0
                # till end of sequence
                while num + count in hash_set:
                    # increment count
                    count += 1

                # if count is more than max_count
                if count > max_count:
                    # update max_count
                    max_count = count

        # return max count
        return max_count


"""
Time complexity: O(n)
Space complexity: O(n)
"""
