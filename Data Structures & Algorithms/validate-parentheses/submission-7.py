class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        brackets= {
            "}":"{",
            "]":"[",
            ")":"(",
            }
        for ch in s:
            if ch not in brackets:
                st.append(ch)
            else:
                if st and st[-1] == brackets[ch]:
                    st.pop()
                else:
                    return False
        return True if len(st) == 0 else False  