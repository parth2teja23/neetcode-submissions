class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        HashMap<Character, Character> hm = new HashMap<>();
        hm.put('}', '{');
        hm.put(']', '[');
        hm.put(')', '(');
        char[] strs = s.toCharArray();
        for(char ch : strs){
            if (hm.containsKey(ch)){
                if (!st.isEmpty() && st.peek() == hm.get(ch)){
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
