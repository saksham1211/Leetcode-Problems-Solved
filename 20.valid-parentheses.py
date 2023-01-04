#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False

                current_char=stack.pop()
                if current_char =="(":
                    if char!=")":
                        return False

                if current_char=="{":
                    if char!="}":
                        return False
                if current_char=="[":
                    if char!="]":
                        return False

        if stack:
            return False
        else:
            return True
            
                
        
# @lc code=end

