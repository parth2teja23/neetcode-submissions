/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        int n = intervals.size();
        int[] start = new int[n];
        int[] end = new int[n];
        int count = 0;
        int maxCount = 0;
        int s= 0;
        int e = 0;


        for(int i = 0; i < intervals.size(); i++){
            start[i] = intervals.get(i).start;
            end[i] = intervals.get(i).end;
        }
        Arrays.sort(start);
        Arrays.sort(end);

        while(s < n){
            if (start[s] < end[e]){
                s++;
                count++;
            } else {
                e++;
                count--;
            }
            maxCount = Math.max(count, maxCount);
        }
        return maxCount;
    }
}
