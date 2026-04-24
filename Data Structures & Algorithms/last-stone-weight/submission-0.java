class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxH = new PriorityQueue<>(Collections.reverseOrder());
        for(int stone : stones){
            maxH.offer(stone);
        }
        while(maxH.size() > 1){
            int stone1 = maxH.poll();
            int stone2 = maxH.poll();
            if (stone1 != stone2){
                maxH.offer(stone1 - stone2);
            }
        }
        if (maxH.isEmpty()){
                return 0;
            } else {
                return maxH.peek();
            }
    }
}