class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        visited = [0] * 26
        for i in range(len(s)):
            visited[ord(s[i])-ord('a')] += 1
            visited[ord(t[i])-ord('a')] -= 1
        for i in visited:
            if i != 0:
                return False
        return True