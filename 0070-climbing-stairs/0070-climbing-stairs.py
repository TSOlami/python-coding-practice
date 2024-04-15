class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, 1

        for i in range(n - 1):
            temp = l
            l = l + r
            r = temp
            
        return l
        