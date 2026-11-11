class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        if len(strs) >= 1 and len(strs) <= 10 ** 4:
            for word in strs:
                counts = [0] * 26

                if len(word) >= 0 and len(word) <= 100:

                    for letter in word:
                        if letter.islower():
                            counts[ord(letter) - ord("a")] += 1

                        else:
                            return False

                    if not tuple(counts) in anagrams:
                        anagrams[tuple(counts)] = []

                    anagrams[tuple(counts)].append(word)

                else:
                    return False
                    
            return anagrams.values()
        
        return False