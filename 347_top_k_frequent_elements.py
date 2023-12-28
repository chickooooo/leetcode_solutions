"""Given an integer array nums and an integer k,
return the k most frequent elements.

You may return the answer in any order.
"""


import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # calculate frequency of each num
        frequency = Counter(nums)

        # will hold tuple of freq & num
        freq_list: list[tuple[int, int]] = []
        # convert freq_list into a heap
        heapq.heapify(freq_list)

        # for each num-freq pair
        for num, freq in frequency.items():
            # if length is less than k
            if len(freq_list) < k:
                # add item to heap
                heapq.heappush(freq_list, (freq, num))
            # otherwise
            else:
                # add item to heap
                # and remove item with least frequency
                heapq.heappushpop(freq_list, (freq, num))

        # return num of all the items in freq list
        return [item[1] for item in freq_list]


"""
Time complexity: O(nlogk)
Space complexity: O(n)
"""
