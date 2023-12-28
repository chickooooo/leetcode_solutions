"""Given an integer array nums,
return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

You must write an algorithm thatruns in O(n) time
and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # initial value of product
        product: int = 1
        # will hold output array
        output: list[int] = []

        # prefix product
        i: int = 0
        while i < len(nums):
            output.append(product)
            product *= nums[i]
            i += 1

        # reset value of product
        product = 1
        # postfix product
        i = len(nums) - 1
        while i >= 0:
            output[i] *= product
            product *= nums[i]
            i -= 1

        # return output array
        return output


"""
Time complexity: O(n)
Space complexity: O(1)
"""
