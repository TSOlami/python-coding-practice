class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Dump all elements from nums2 into the end of nums1
        last1, last2 = len(nums1) - 1, len(nums2) - 1

        for i in range(len(nums2)):
            nums1[last1] = nums2[last2]
            last1, last2  = last1 - 1, last2 - 1

        # Make sure new nums1 is sorted
        nums1.sort()    # Will write logic for merge sort later
