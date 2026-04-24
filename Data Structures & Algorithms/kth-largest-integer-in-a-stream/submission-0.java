class KthLargest {
    private int k;
    private PriorityQueue<Integer> minH;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minH = new PriorityQueue<>();
        for(int num : nums){
            minH.offer(num);
            if (minH.size() > k){
                minH.poll();
            }
        }
    }
    
    public int add(int val) {
        minH.offer(val);
        if (minH.size() > k){
            minH.poll();
        }
        return minH.peek();
    }
}
