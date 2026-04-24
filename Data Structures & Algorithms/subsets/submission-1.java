class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        helper(nums, 0, res, subset);
        return res;
    }
    private void helper(int[] nums, int i, List<List<Integer>> res, List<Integer> subset){
        if (i == nums.length){
            res.add(new ArrayList<>(subset));
            return;
        }
        // with i
        subset.add(nums[i]);
        helper(nums, i+1, res, subset);
        // without i
        subset.remove(subset.size() - 1);
        helper(nums, i+1, res, subset);
    }
}
