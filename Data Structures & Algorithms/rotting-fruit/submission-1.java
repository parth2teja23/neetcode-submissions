class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;
        int time = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1){
                    fresh++;
                }
                if (grid[i][j] == 2){
                    q.add(new int[] {i, j});
                }
            }
        }
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while(!q.isEmpty() && fresh > 0){
            int length = q.size();
            for(int i = 0; i < length; i++){
                int[] cur = q.poll();
                int r = cur[0];
                int c = cur[1];
                for(int[] direction : directions){
                    int row = r + direction[0];
                    int col = c + direction[1];
                    if (row < grid.length && row >= 0 && col < grid[0].length && col >= 0 && grid[row][col] == 1){
                        grid[row][col] = 2;
                        q.add(new int[]{row, col});
                        fresh--;
                    }
                }
                
            } 
            time++;
        }
        return fresh == 0 ? time : -1;
    }
}
