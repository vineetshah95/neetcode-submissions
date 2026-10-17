class Solution {
    public int maxArea(int[] heights) {
        //Initialize 2 variables left and right
        // run while (left pointer is less than right pointer)
        //calculate area == left + right * math.min(height[left], height[right])
        //Update maxArea using Math.max()
        //MOve pointer according to shorter height
        //Retun max

        int left = 0;
        int right = heights.length-1;
        int maxArea = -1;
        while(left < right){
            int width = right-left;
            int height = Math.min(heights[left], heights[right]);
            int area = width * height;
            maxArea = Math.max(maxArea, area);
            if(heights[left] < heights[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return maxArea;
    }
}
