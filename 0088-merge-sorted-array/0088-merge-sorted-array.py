class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set pointers
        i = m - 1  # Last real element in nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # End of nums1

        # Merge from back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If anything left in nums2, copy it
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
