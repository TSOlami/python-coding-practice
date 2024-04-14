class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert x to a string and compare it with its reverse
        return str(x) == str(x)[::-1]
        