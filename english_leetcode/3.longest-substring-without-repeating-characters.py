class Solution:
    def lengthOfLongestSubstring(self, s):
        usedChar = {}
        start = max_length = 0
        for index, char in enumerate(s):
            if char in usedChar and start<=usedChar[char]:
                start = usedChar[char] + 1
            else:
                max_length = max(max_length, index-start+1)
            usedChar[char] = index
        return max_length
