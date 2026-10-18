class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        int maxFrequency = 0;
        int[] count = new int[26];
        int maxLength = 0;
        for(int right = 0; right < s.length(); right++){
            // Step 1: Update character frequency
            count[s.charAt(right) - 'A']++;
            // Step 2: Find maxFrequency
            maxFrequency = Math.max(maxFrequency, count[s.charAt(right) - 'A']);
            // Step 3: Shrink window if invalid
            while((right - left + 1)-maxFrequency > k){
                count[s.charAt(left) - 'A']--;
                left++; 
            }

            // Step 4: Update maxLength
            maxLength = Math.max(maxLength, right-left+1);
        }
        return maxLength;
    }
}
