#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not operations:
            return None
        stack=[]

        for item in operations:
            if item not in ['+', 'D', 'C']:
                stack.append(int(item))
                print(stack)

            else:
                if item=="C":
                    stack.pop()
                    print(stack)

                if item=="D":
        
                    ele=int(stack.pop())
                    stack.append(ele)
                    stack.append(2*ele)
                    print(stack)

                if item=="+":
                    ele1=int(stack.pop())
                    print(stack)
                    ele2=int(stack.pop())
                    print(stack)
                    stack.append(ele2)
                    stack.append(ele1)
                    stack.append(ele1+ele2)
                    


        return sum(stack)
# @lc code=end

