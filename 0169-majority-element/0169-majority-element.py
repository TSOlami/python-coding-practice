class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Set a dictionary and map each num in nums (key) to the number of times they appear (value)
        seen = {}
        i = 0

        while i < len(nums):
            num = nums[i]

            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

            if seen[num] > len(nums) // 2:
                return num

            i += 1
