class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) >= 1 and len(nums) <= 10 ** 5:
            new_set = set(nums)

            for num in new_set:
                if not num >= (-10) ** 9 and not num <= 10 ** 9:
                    break

            else:
                if len(nums) == len(new_set):
                    return False

                return True