class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> map = new HashMap<>();
        
        for(char c: s.toCharArray()){
            map.put(c, map.getOrDefault(c,0)+1);
        }
        for(char a: t.toCharArray()){
            map.put(a, map.getOrDefault(a,0)-1);
        }
        for(int count: map.values()){
            if(count !=0){
                return false;
            }
            
        }
        return true;
    }
}
