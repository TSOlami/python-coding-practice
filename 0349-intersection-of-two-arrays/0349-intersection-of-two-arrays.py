class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []
        for i in nums1:
            for j in nums2:
                if i == j and i not in seen:
                    result.append(i)
                    seen[i] = 1
                    break
        return result
                    