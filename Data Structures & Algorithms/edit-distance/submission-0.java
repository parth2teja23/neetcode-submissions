class Solution {
    public int minDistance(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        //   abc
        // z[][][][5]
        // a[][][][4]
        // b[][][][3]
        // c[][][][2]
        // d[][][][1]
        //  [3][2][1][0]

        int[][] dp = new int[n+1][m+1];
        for(int i = 0; i <= n; i++){
            // Fill last column
            dp[i][m] = n-i;
        }
        for(int j = 0; j <= m; j++){
            // Fill last row
            dp[n][j] = m-j;
        }
        for(int i = n-1; i>= 0; i--){
            for(int j = m-1; j>= 0; j--){
                if (word1.charAt(i) == word2.charAt(j)){
                    dp[i][j] = dp[i+1][j+1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i+1][j+1], Math.min(dp[i][j+1], dp[i+1][j]));
                }
            }
        }
        return dp[0][0];
    }
}
