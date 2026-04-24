class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        int days = 0;
        for(int i = 0; i < temperatures.length; i++){
            for(int j = i; j < temperatures.length; j++){
               if (temperatures[j] > temperatures[i]){
                days = j-i;
                result[i] = days;
                break;
               } 
            }
        }
        return result;
    }
}
