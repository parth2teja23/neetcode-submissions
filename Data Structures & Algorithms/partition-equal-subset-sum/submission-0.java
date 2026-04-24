class Solution {
    public boolean canPartition(int[] nums) {
        if (Arrays.stream(nums).sum() % 2 != 0) {
            return false;
        }

        int target = Arrays.stream(nums).sum() / 2;
        Set<Integer> dp = new HashSet<>();
        dp.add(0);
        for(int i = 0; i < nums.length; i++){
            Set<Integer> nextDP = new HashSet<>();
            for(int t : dp){
                if (t + nums[i] == target) return true;
                nextDP.add(t + nums[i]);
                nextDP.add(t);
            }
            dp.addAll(nextDP);
        }
        return false;
    }
}
