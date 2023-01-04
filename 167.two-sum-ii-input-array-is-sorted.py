#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start

class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r=0, len(numbers)-1

        while(l<r):
            ans=numbers[l]+numbers[r]
            if ans==target:
                return [l+1, r+1]

            if ans<target:
                l+=1
            else:
                r-=1

        
        
            

            

            
# @lc code=end

