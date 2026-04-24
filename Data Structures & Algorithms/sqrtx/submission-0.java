class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1) return x;
        int l = 0;
        int r = x;
        int mid = -1;
        while(l <= r){
            mid = l + (r - l) / 2;
            long sqr = (long) mid * mid;
            if (sqr == x) {
                return mid;
            } else if (sqr <= x){
                l = mid +1;
            } else {
                r = mid - 1;
            }
        }
        return r;
    }
}