class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //Create HashMap
        //For each num in nums increase frequency of nums in hashMap
        //Create MinHeap - compare numbers based on their frequency
        //for each key in hashmap - add key in min heap
        //if heap size is > k, remove element of lowest frequency
        //create result array to size k
        //for(0 to k-1)- heap.poll


        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        PriorityQueue<Integer>minHeap = new PriorityQueue<>((a,b)-> Integer.compare(map.get(a), map.get(b)));
        for(int num: map.keySet()){
            minHeap.offer(num);
            if(minHeap.size() > k){
                minHeap.poll();
            }
        }
        int[] result = new int[k];
        for(int i = 0; i < k; i ++){
            result[i] = minHeap.poll();
        }
        return result;
    }
}
