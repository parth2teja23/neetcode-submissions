class Solution {
    private Map<Integer, ArrayList<Integer>> adj = new HashMap<>();
    private Set<Integer> visited = new HashSet<>();

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for(int i = 0; i < numCourses; i++){
            adj.put(i, new ArrayList<>());
        }
        for(int i = 0; i < prerequisites.length; i++){
            int course = prerequisites[i][0];
            int pre = prerequisites[i][1];
            adj.get(course).add(pre);
        }
        for(int c = 0; c < numCourses; c++){
            if(!dfs(c)){
                return false;
            }
        }
        return true;
    }
    private boolean dfs(int course){
        if (visited.contains(course)){
            return false;
        }
        if (adj.get(course).isEmpty()){
            return true;
        }
        visited.add(course);
        for(int pre : adj.get(course)){
            if (!dfs(pre)){
                return false;
            }
        }
        visited.remove(course);
        adj.put(course, new ArrayList<>());
        return true;
    }
}
