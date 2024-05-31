class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Set the initial value for the XOR operation
        singleNum = 0
        
        # XOR every element of the array
        for num in nums:
            singleNum = singleNum ^ num
            
        return singleNum