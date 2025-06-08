class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top_1 = top_2 = top_3 = None

        for num in nums:
            if num == top_1 or num == top_2 or num == top_3:
                continue

            if top_1 is None or num > top_1:
                top_3 = top_2
                top_2 = top_1
                top_1 = num
            elif top_2 is None or num > top_2:
                top_3 = top_2
                top_2 = num
            elif top_3 is None or num > top_3:
                top_3 = num

        return top_3 if top_3 is not None else top_1
