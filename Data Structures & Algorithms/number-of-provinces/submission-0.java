class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int res = 0;
        for(int i = 0; i < n; i++){
            if (!visited[i]){
                dfs(i, isConnected, visited, n);
                res++;
            }
        }
         return res;
    }
   
    public void dfs(int node, int[][] isConnected, boolean[] visited, int n){
        visited[node] = true;
        for(int nbr = 0; nbr < n; nbr++){
            if (isConnected[node][nbr] == 1 && !visited[nbr]){
                dfs(nbr, isConnected, visited, n);
            }
        }
    }

}
