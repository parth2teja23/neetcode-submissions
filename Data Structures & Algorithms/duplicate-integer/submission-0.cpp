class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set <int> ans;
        for (int i = 0; i < nums.size(); i++){
            if (ans.find(nums[i]) != ans.end()){
                return true;
            }
            else {
                ans.insert(nums[i]);
            }
        }
        return false;
    }
};
