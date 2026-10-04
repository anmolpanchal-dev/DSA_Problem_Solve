class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        t_freq = {}
        for word in range(len(s)):
            s_freq[s[word]] = s_freq.get(s[word],0) + 1
            t_freq[t[word]] = t_freq.get(t[word],0) + 1
        if s_freq != t_freq:
            return False
        return True
        