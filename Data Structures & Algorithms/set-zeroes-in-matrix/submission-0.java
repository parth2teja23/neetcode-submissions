class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        boolean[] rowZero = new boolean[rows + 1];
        boolean[] colZero = new boolean[cols + 1];
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if (matrix[i][j] == 0){
                    rowZero[i] = true;
                    colZero[j] = true;
                }
            }
        }
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if  (rowZero[i] == true || colZero[j] == true){
                    matrix[i][j] = 0;
                }
            }
        }

    }
}