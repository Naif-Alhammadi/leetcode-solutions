class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            if len(s) >= 1 and len(t) <= 5 * (10 ** 4):
                count_s, count_t = {}, {}

                for count in s:
                    if not count.islower():
                        return False
                    count_s[count] = 1 + count_s.get(count, 0)



                for count in t:
                    if not count.islower():
                        return False
                    count_t[count] = 1 + count_t.get(count, 0)

                if count_s != count_t:
                    return False

                return True


        else:
            return False