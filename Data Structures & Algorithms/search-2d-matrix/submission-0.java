class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Flatten the array
        int[] arr = new int[matrix.length * matrix[0].length];
        int k = 0;
        for (int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[i].length; j++){
                arr[k] = matrix[i][j];
                k++;
            }
        }
        // Perform the binary Search
        int l = 0;
        int r = arr.length - 1;
        while (l <= r){
            int mid = (l + r) / 2;
            if (target < arr[mid]){
                r = mid - 1;
            } else if (target > arr[mid]) {
                l = mid + 1;
            } else{
                return true;
            }
        }
        return false;
    }
}
