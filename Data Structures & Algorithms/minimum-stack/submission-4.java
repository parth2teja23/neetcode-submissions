class MinStack {
    private Stack<Integer> st;
    private Stack<Integer> minSt;
    
    public MinStack() {
        st = new Stack<>();
        minSt = new Stack<>();
    }
    
    public void push(int val) {
        if ((minSt.isEmpty()) || val <= minSt.peek()){
            st.push(val);
            minSt.push(val);
        } else {
            st.push(val);
        }
    }
    
    public void pop() {
        if (st.isEmpty()) return;
        int top = st.pop();
        if (top == minSt.peek()) minSt.pop();
    }
    
    public int top() {
        return st.peek();
    }
    
    public int getMin() {
        if (!st.isEmpty()){
            return minSt.peek();
        } else {
            return 0;
        }
    }
}
