class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diffs = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
            if len(diffs) > 2:
                return False
        
        if len(diffs) == 0:
            return True
        
        if len(diffs) == 1:
            return False
        
        i, j = diffs[0], diffs[1]
        return s1[i] == s2[j] and s1[j] == s2[i]