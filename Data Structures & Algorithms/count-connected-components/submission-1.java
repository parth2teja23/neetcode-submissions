class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> res = new ArrayList<>();
        int[] visited = new int[n+1];
        for(int i = 0; i < n; i++){
            res.add(new ArrayList<>());
        }
        for(int[] edge : edges){
            res.get(edge[0]).add(edge[1]);
            res.get(edge[1]).add(edge[0]);
        }
        int count = 0;
        for(int i = 0; i < n; i++){
            if (visited[i] == 0){
                dfs(res, visited, i);
                count++;

            }
        }
        return count;
    }
    private void dfs(List<List<Integer>> res, int[] visited, int i){
        visited[i] = 1;
        for(int nei : res.get(i)){
            if (visited[nei] == 0){
                dfs(res, visited, nei);
            }
        }
    }
}
