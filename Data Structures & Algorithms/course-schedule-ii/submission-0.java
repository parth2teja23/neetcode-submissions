class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for(int i = 0; i < numCourses; i++){
            adj.add(new ArrayList<>());
        }
        for(int[] pre : prerequisites){
            int req = pre[0];
            int course = pre[1];
            indegree[req]++;
            adj.get(course).add(req);
        }
        Queue<Integer> q = new LinkedList<>();
        int[] output = new int[numCourses];
        int finished = 0;
        for(int i = 0; i < numCourses; i++){
            if (indegree[i] == 0) q.add(i);
        }

        while(!q.isEmpty()){
            int node = q.poll();
            output[finished] = node;
            finished++;
            for(int nei : adj.get(node)){
                indegree[nei]--;
                if(indegree[nei] == 0) q.add(nei);
            }
        }
        if (finished != numCourses){
        return new int[0];

        }
    return output;
    }
    
}
