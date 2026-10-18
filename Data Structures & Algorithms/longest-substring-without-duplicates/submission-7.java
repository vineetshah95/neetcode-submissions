class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int left = 0;
        int maxLength = 0;
        
        for(int right = 0; right < s.length(); right++){
            while(set.contains(s.charAt(right))){
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            maxLength = Math.max(maxLength, right-left+1);
        }
        return maxLength;
    }
}


/*
zxyzxyz = 3 xyz
left pointer and right pointer at 0
length = 0;
maxLength = 0;


We will start both our pointers from left at 0,
So currently our window is empty
we will have a global maxLength to store our result
we will also have a local length variable to store our window length

We start with for right as end of the window
for right = 0; right less than string.length() and right++
we will iterate and add it into our hashSet(becase set cannot contain duplicates)
if any duplicate occurs we calucalte our maxlength and make our local length as 0
move our left pointer to right and iterate again

at the last we return maxLength

*/