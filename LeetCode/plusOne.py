class Solution:
    def plusOne(self, digits: list) -> list[int]:
        id = 0
        carry = 1

        digits.reverse()

        while carry:
            if id < len(digits): 
                if digits[id] == 9:
                    digits[id] = 0
                elif digits[id] < 9:
                    digits[id] +=1
                    carry = 0
            else:
                digits.append(1)
                carry = 0

            id+=1
            
            
        digits.reverse()

        return digits


sol = Solution
longest = []
for i in range(10000000):
    longest.append(9)

print( sol.plusOne(sol, [9]) )
print( sol.plusOne(sol, [9,9,9]) )
print( sol.plusOne(sol, [1,9,9]) )
print( sol.plusOne(sol, longest) )
        
                
