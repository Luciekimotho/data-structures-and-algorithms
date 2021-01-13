class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sset = set()
        for i, num in enumerate(nums):
            other = target - num
            if other in sset:
                return nums.index(other), i
            else:
                sset.add(num)