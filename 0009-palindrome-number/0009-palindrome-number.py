class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1

        while x  >= div:
            div *= 10

        div /= 10
        while div // 10 != 0:
            right = x % 10
            left = x // div
            if left != right:
                return False
            
            x //= 10
            div /= 10
            x %= div
            div /= 10
            
        return True

