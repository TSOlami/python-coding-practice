class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        expected_sum = 0
        for i in range(n + 1):
            expected_sum += i

        actual_sum = sum(nums)

        return expected_sum - actual_sum
