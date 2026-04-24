class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> countMap = new HashMap<>();
        List<Integer>[] buckets = new List[nums.length + 1];
        int[] res = new int[k];
        for(int n : nums){
            countMap.put(n, countMap.getOrDefault(n,0) + 1);
        }
        for(int key : countMap.keySet()){
            int freq = countMap.get(key);
            if (buckets[freq] == null) buckets[freq] = new ArrayList<>();
            buckets[freq].add(key);

        }
        int count = 0;
        for(int i = buckets.length-1; i >= 0 && count < k; i--){
            if (buckets[i] != null){
                for(int num : buckets[i]){
                    res[count] = num;
                    count++;
                    if (count == k) return res;
                }
            }
        }
        return res;
    }
}
