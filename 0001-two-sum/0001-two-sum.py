class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) >= 2 and len(nums) <= 10 ** 4 and target >= -10 ** 9 and target <= 10 ** 9:
            l_index = 0

            while True:
                try:
                    left = nums[l_index]
                    if not (left >= -10 ** 9 and left <= 10 ** 9):
                        return False


                except IndexError:
                    return []
                
                for i in range(len(nums) - l_index - 1):
                    right = i + 1 + l_index
                    if nums[right] >= -10 ** 9 and nums[right] <= 10 ** 9:
                        sum = left + nums[right]
                        if sum == target:
                            return  [l_index, right]

                l_index += 1 
        else:
            return []