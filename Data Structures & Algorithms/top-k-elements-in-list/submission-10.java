class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        // {1 -> 3
        // 2 -> 2
        // 3 -> 1}
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a,b) -> Integer.compare(map.get(a), map.get(b)));
        for(int num: map.keySet()){
            minHeap.offer(num);
            if(minHeap.size() > k){
                minHeap.poll();
            }
        }
        int[] result = new int[k];
        for(int i=0; i<k; i++){
            result[i] = minHeap.poll();
        }
        return result;
    }
}

//Create Hashmap of frequency
// add frequency 

// for every value in map create Priority queue with minHeap
//and compare the values 
// when 1 will come it will be add in the minheap 
// then 2 will come it will be added in minheap 
// then 3 will come but here the k = 2 so we will add a condition,
// if while adding the values to minHeap if it exceeds k,
// we poll out the value

// after that for every value in minheap till k we poll into a new int[] result