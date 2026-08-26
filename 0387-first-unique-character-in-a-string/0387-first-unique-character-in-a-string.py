class Solution(object):
    def firstUniqChar(self, s):
        result={}

        for ch in s:
            if ch in result:
                result[ch]+=1
            else:
                result[ch]=1

        for i in range(len(s)):
            if result[s[i]] == 1:
                return i

        return -1

