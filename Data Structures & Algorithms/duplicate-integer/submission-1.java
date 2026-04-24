class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> mySet = new HashSet<Integer>();
        for(int i : nums){
            if (mySet.contains(i)){
                return true;
            }
            else {
                mySet.add(i);
            }
        }
        return false;
    }
}
