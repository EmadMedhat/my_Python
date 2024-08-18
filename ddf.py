class Solution:
    def longestCommonSubsequenceLength(self, s1, s2):
        cache = [[0 for i in range(0, len(s1) + 1)] for i in range (0, len(s2) + 1)]
        
        for s2Row in range(0,len(s2)+1):
            for s1Col in range(0,len(s1)+1):
                if (s2Row == 0 or s1Col == 0) :
                    cache[s2Row][s1Col]=0
                elif (s2[s2Row-1] == s1[s1Col-1]):
                    cache[s2Row][s1Col] = cache[s2Row - 1][s1Col - 1] + 1
                else :
                    cache[s2Row][s1Col] = max(cache[s2Row - 1][s1Col], cache[s2Row][s1Col - 1])

        return cache[len(s2)][len(s1)]
s1 = "sssDBsssfhfhfsssshD"
s2 = "sssCfssgdfgdfgdfsssgBD"
ss=Solution()
print(ss.longestCommonSubsequenceLength(s1,s2))