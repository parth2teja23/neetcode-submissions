class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        HashMap<Character, Character> brackets = new HashMap<>();
        brackets.put('}', '{');
        brackets.put(')', '(');
        brackets.put(']', '[');
        for(Character ch : s.toCharArray()){
            if (brackets.containsKey(ch)){
                if (!st.isEmpty() && st.peek() == brackets.get(ch)){
                    st.pop();
                } else {
                    return false;
                }
            } else {
                st.push(ch);
            }
        }
        return st.isEmpty();
    }
}
