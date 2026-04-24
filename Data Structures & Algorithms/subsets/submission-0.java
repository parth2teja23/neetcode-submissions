class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        int i = 0;
        dfs(nums, i, res, subset);
        return res;
    }
    private void dfs(int[] nums, int i, List<List<Integer>> res, List<Integer> subset){
        // base case
        if (i == nums.length){
            res.add(new ArrayList<>(subset));
            return;
        }
        // recursive call when we include the element.
        subset.add(nums[i]);
        dfs(nums, i+1, res, subset);
        // recursive call when we dont include the element.
        subset.remove(subset.size() -1);
        dfs(nums, i+1, res, subset);
    }
}
