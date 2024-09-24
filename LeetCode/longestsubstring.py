in1 = "abcabcaa"
in2 = "bbbbb"
in3 = "pwwkew"
in4 = " "
in5 = "dvdf"

def lengthOfLongestSubstring(s: str) -> int:
    letter_index = {}  # To store the most recent index of each character
    left = 0  # left side of sliding window
    longest = 0
    
    for right in range(len(s)): # right side of sliding window
        letter = s[right]
        
        if letter in letter_index and letter_index[letter] >= left:
            # move left pointer to last appearance
            left = letter_index[letter] + 1
        
        letter_index[letter] = right
        longest = max(longest, right - left + 1)
    
    return longest

print(lengthOfLongestSubstring(in1))
print(lengthOfLongestSubstring(in2))
print(lengthOfLongestSubstring(in3))
print(lengthOfLongestSubstring(in4))
print(lengthOfLongestSubstring(in5))
