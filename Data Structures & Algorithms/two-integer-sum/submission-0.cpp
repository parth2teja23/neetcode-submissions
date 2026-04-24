class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>myMap;
        for(int i  = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if (myMap.find(diff) != myMap.end()){
                return {myMap[diff], i};
            }
            myMap[nums[i]] = i;
        }
        return {};
    }
};
