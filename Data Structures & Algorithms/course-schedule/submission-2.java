class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for(int i  = 0; i < numCourses; i++){
            adj.add(new ArrayList<>());
        }
        for(int[] pair : prerequisites) {
            int course = pair[0];
            int requirement = pair[1];
            indegree[course]++;
            adj.get(requirement).add(course);
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < numCourses; i++){
            if (indegree[i] == 0) q.add(i);
        }
        int finished = 0;
        while(!q.isEmpty()){
            int node = q.poll();
            finished++;
            for(int nei : adj.get(node)){
                indegree[nei]--;
                if (indegree[nei] == 0) q.add(nei);
            }
        }
        return finished == numCourses;
    }
}
