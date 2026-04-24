class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n + 1];
        Arrays.fill(memo, -1);
        return dp(n, memo);
    }
    private int dp(int n, int[] memo){
        if (n < 0){
            return 0;
        } else if (n == 0){
            return 1;
        } else if (memo[n] != -1) {
            return memo[n];
        } else {
            memo[n] = dp(n-1, memo) + dp(n-2, memo);
            return memo[n];
        }
    }
}
