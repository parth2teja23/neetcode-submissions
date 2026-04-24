class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // Step 1 - Store position and speed together
        int n = position.length;
        int[][] cars = new int[n][2];
        for(int i = 0; i < n; i++){
            cars[i][0] = position[i]; // Car position
            cars[i][1] = speed[i]; // Car speed
        } 
        // Step 2 - Sort cars from right to left (descending order)
        Arrays.sort(cars, (a,b) -> b[0] - a[0]);

        // Step 3 - Use Stack to store car fleet
        Stack<Double> st = new Stack<>();
        for(int i = 0; i < n; i++){
            int carPos = cars[i][0];
            int carSpeed = cars[i][1];
        // Step 4 - Calculate time taken to reach the target
        double time = (double) (target - carPos) / carSpeed;
        // Push the time to stack
        st.push(time);

        // Step 5 - If the car reaches next to it, the will form fleet
        // So we have to remove it from stack
        if (st.size() >= 2){
        double lastCarTime = st.pop();
        double aheadTime = st.peek();
        if (lastCarTime > aheadTime) {
            st.push(lastCarTime);
        }
        }
        }
        return st.size();
    }
}
