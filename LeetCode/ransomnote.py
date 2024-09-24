class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for letter in ransomNote:
            try:
                magazine.index(letter)
                magazine = magazine.replace( letter , '' , 1 )
            except ValueError:
                return False

        return True
        
res1 = Solution.canConstruct(Solution, "asdf", "asdf")
res2 = Solution.canConstruct(Solution, "asdf", "asd")
res3 = Solution.canConstruct(Solution, "aa", "aad")
res4 = Solution.canConstruct(Solution, "aa", "ab")

print("Done.")