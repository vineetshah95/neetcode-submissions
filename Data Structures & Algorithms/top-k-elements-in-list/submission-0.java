class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int count =0;
        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        int[] result = new int[k];
        for(int i = 0; i<k; i++){
            int maxFrequency = 0;
            int maxValue= result[i];
            for(Map.Entry<Integer, Integer> entry: map.entrySet()){
                if(entry.getValue() > maxFrequency){
                    maxFrequency = entry.getValue();
                    maxValue = entry.getKey();   
                }
            }
            result[i] = maxValue;
            map.remove(result[i]);
        }
        return result;
    }
}
