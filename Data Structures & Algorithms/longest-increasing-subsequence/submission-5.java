class Solution {
    public int lengthOfLIS(int[] nums) {
        return helper(nums, 0, -1);
    }
    public int helper(int[] nums, int i, int prev){
        if (i == nums.length){
            return 0;
        }
        int res = helper(nums, i+1, prev); // No take
        if (prev == -1 || nums[prev] < nums[i]){
            res = Math.max(res, 1 + helper(nums, i+1, i));
        }
        return res;
    }
}
