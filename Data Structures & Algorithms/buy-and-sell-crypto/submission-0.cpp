class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int leftPtr = 0;
        int rightPtr = 1;
        int maxP = 0;
        int profit = 0;
        while (rightPtr < prices.size()){
            if (prices[leftPtr] < prices[rightPtr]){
                profit = prices[rightPtr] - prices[leftPtr];
                maxP = max(maxP, profit);

            } else {
                leftPtr = rightPtr;
            }
            rightPtr++;
        }
        return maxP;
    }
};
