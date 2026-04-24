class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = 0;
        int area = 0;
        int maxArea = 0;
        for(int i = 0; i < heights.length; i++){
            left = i;
            for(int j = i; j < heights.length; j++){
                right = j;
                area = (right-left) * Math.min(heights[left], heights[right]);
                maxArea = Math.max(area, maxArea);
            }
        }
        return maxArea;
    }
}
