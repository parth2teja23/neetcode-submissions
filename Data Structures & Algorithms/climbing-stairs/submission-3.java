class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n +1];
        Arrays.fill(memo, -1);
        return dp(memo, n);
    }
    private int dp(int[] memo, int n){
        if (n == 0) {
            return 1;
        } else if (n < 1) {
            return 0;
        } else if (memo[n] != -1) return memo[n];
        memo[n] = dp(memo, n-1) + dp(memo, n-2);
        return memo[n];
    }

    // if (n == 0 || n == 1) return 1;
    // return climbStairs(n - 1) + climbStairs(n - 2);
}
