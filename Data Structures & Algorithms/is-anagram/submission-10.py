class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited = [0] * 26

        for ch in s:
            visited[ord(ch) - ord('a')] += 1
        for ch in t:
            visited[ord(ch) - ord('a')] -= 1
        
        for i in visited:
            if i != 0:
                return False
        return True