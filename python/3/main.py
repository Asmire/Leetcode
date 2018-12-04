class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        lo = 0
        res = 0
        for i in range(len(s)):
            if s[i] in dic and lo <= dic[s[i]]:
                lo = dic[s[i]] + 1
            else:
                res = max(res, i - lo  + 1)
            dic[s[i]] = i
        return res


    def lengthOfLongestSubstring(self, s):
        dic = {}
        res, lo = 0, -1
        for i, c in enumerate(s):
            if c in dic and lo < dic[c]:
                lo = dic[c]
            res = max(res, i - lo)
            dic[c] = i
        return res
