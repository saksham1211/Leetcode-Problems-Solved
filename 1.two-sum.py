


#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from ctypes.wintypes import tagRECT


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic={}
        
        for i in range(len(nums)):
            ans=target-nums[i]

            if ans not in dic:
                dic[ans]=i
        print(dic)
        for i in range(len(nums)):
            if ((target-nums[i]) in dic):
                return [i, dic[target-nums[i]]]



        
        
# @lc code=end

