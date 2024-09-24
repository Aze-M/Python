
class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        answer = 0

        for string in patterns:
            if string in word:
                answer +=1
        
        return answer