
class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) return 0;
        int res = nums[0];
        int curMin = 1;
        int curMax = 1;
        for(int num : nums){
            int prevMax = curMax;
            int prevMin = curMin;
            curMax = Math.max(Math.max(num * prevMin,num * prevMax), num);
            curMin = Math.min(Math.min(num * prevMin,num * prevMax), num);
            res = Math.max(res, curMax);
        }
        return res;
    }
}