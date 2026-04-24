class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        for(int i = 0; i < n; i++){
            prefix[i + 1] = prefix[i] + nums[i];
        }
        for(int i = 0; i < n; i++){
            if (prefix[i] == prefix[n] - prefix[i + 1]) return i;
        }
        return -1;
    }
}