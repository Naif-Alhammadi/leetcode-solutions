class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) >= 2 and len(nums) <= 10 ** 4 and target >= -10 ** 9 and target <= 10 ** 9:
            difs = {}

            for i in range(len(nums)):

                if not (nums[i] >= -10 ** 9 and nums[i] <= 10 ** 9):
                    return []
                
                dif = target - nums[i]

                if nums[i] in difs:
                    return [difs[nums[i]], i]
                
                difs[dif] = i
                    

            return []

        else:
            return []