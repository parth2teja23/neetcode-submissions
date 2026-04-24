class Solution {
    public int maxProfit(int[] prices) {
        int right = 1;
        int left = 0;
        int p = 0;
        int maxP = 0;
        while (right < prices.length){
            if (prices[right] >prices[left]){
                p = prices[right] - prices[left];
                maxP = Math.max(p, maxP);
                
            }
            else {
                left = right;
            }
            right++;
        }
        return maxP;
    }
}
