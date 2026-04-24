class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        visitedRansom = [0] * 26
        visitedMag = [0] * 26

        for ch in ransomNote:
            visitedRansom[ord(ch) - ord('a')] += 1
        for ch in magazine:
            visitedMag[ord(ch) - ord('a')] += 1
        
        for i in range(len(visitedRansom)):
            if visitedRansom[i] > visitedMag[i]:
                return False
        return True
            
         
