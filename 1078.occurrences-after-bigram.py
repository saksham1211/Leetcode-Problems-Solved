#
# @lc app=leetcode id=1078 lang=python3
#
# [1078] Occurrences After Bigram
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text=list(text.split())

        result=[]
        for i in range(0, len(text)-2):
            if text[i]==first and text[i+1]==second:
                result.append(text[i+2])

        return result


# @lc code=end

