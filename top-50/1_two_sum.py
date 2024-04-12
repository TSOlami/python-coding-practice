class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_nums = {}

        # Traverse through the elements of the array
        for i , num in enumerate(nums):
            compliment = target - num

            if compliment in seen_nums:
                return seen_nums[compliment], i
            else:
                seen_nums[num] = i
        
        return []