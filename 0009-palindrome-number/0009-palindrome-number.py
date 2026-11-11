class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= -2 ** 31 and x <= 2 ** 31:
            length = len(str(x))
            REDUCED_SIZE = 1

            while True:
                right = x % 10
                left = x // 10 ** (length - REDUCED_SIZE)
                if left == right:
                    x //= 10
                    length -= 1
                    x %= 10 ** (length - REDUCED_SIZE)
                    length -= 1
                    if length <= 0:
                        return True
                else:
                    return False
                if length == 0:
                    return False        