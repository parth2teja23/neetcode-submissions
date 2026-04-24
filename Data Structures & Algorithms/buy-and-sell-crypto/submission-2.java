class Solution {
    public int maxProfit(int[] prices) {
        int l = 0, r = 1, p = 0, maxP = 0;
        while(r < prices.length){
            if (prices[r] > prices[l]){
                p = prices[r] - prices[l];
                maxP = Math.max(p, maxP);
            } else {
                l = r;
            }
            r++;
        }
        return maxP;
    }
}
