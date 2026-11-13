class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        s_len = len(s)

        if s_len < 1 or s_len > 15:
            return False
        
        ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = 0
        
        for i in range(s_len):
            value = 0
            if s[i] not in ROMAN:
                return False
            
            if s[i] == "I" and s_len - 1 != i:
                if s[i + 1] in ["V", "X"]:
                    value = ROMAN[s[i]]

            elif s[i] == "X" and s_len - 1 != i:
                if s[i + 1] in ["L", "C"]:
                    value = ROMAN[s[i]]

            elif s[i] == "C" and s_len - 1 != i:
                if s[i + 1] in ["D", "M"]:
                    value = ROMAN[s[i]]

            sum += ROMAN[s[i]] - value - value


        if sum < 1 or sum > 3999:
            return False
        
        return sum
        # Time: O(n)
        # Space: O(1)