class Solution {
    public List<List<Integer>> permute(int[] nums) {
        // Bit Mask:
        List<List<Integer>> res = new ArrayList<>();
        bitMask(new ArrayList<>(), nums, 0, res);
        return res;
    }
    private void bitMask(List<Integer> perm, int[] nums, int mask, List<List<Integer>> res){
        if (perm.size() == nums.length){
            res.add(new ArrayList<>(perm));
            return;
        }
        for(int i = 0; i < nums.length; i++){
            if ((mask & (1 << i)) == 0){
                perm.add(nums[i]);
                bitMask(perm, nums, mask | (1 << i), res );
                perm.remove(perm.size() - 1);
            }
        }
    }

}
