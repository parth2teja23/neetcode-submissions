class Solution {
    public int sumOfSquares (int n) {
        int res = 0;
        while (n > 0){
            res += Math.pow((n % 10) , 2);
            n = n / 10;
        }
        return res;
    }
    public boolean isHappy(int n) {
        int slow = n;
        int fast = sumOfSquares(n);
        while (slow != fast) {
            slow = sumOfSquares(slow);
            fast = sumOfSquares(sumOfSquares(fast));
        }

        return slow == 1;
    }
}
