class Solution {
    private int[][] dp;
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        dp = new int[n][n+1];
        for(int[] row : dp){
            Arrays.fill(row, -1);
        }
        return helper(nums, 0, -1);
    }
    public int helper(int[] nums, int i, int prev){
        if (i == nums.length){
            return 0;
        }
        if (dp[i][prev+1] != -1){
            return dp[i][prev+1];
        }
        int res = helper(nums, i+1, prev); // No take
        if (prev == -1 || nums[prev] < nums[i]){
            res = Math.max(res, 1 + helper(nums, i+1, i)); // Take
        }
        dp[i][prev+1] = res;
        return res;
    }
}
