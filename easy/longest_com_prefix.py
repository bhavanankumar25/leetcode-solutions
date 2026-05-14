class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        for i in range(len(strs[0])): 
            for word in strs:          # check every word
                if i >= len(word) or word[i] != strs[0][i]:
                    return prefix      #if mismatch found, stop
            prefix += strs[0][i]      
        return prefix

#take first word as reference - strs[0]
#Outer loop - goes through each position (0, 1, 2...)
#Inner loop - checks every word at that position
#i >= len(word) - word is too short, stop
#word[i] != strs[0][i] - character doesn't match first word, stop
#prefix += strs[0][i] - all words matched at this position, add character to prefix