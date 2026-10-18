class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = left+1; 
        int maxProfit = 0;
        while(right< prices.length){
            if(prices[left]> prices[right]){
                left = right;
            }
            else{
                int profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            }
            right++;
        }
        return maxProfit;
    }
}

/*
[10,2,5,6,7,1]
    left 
        right


Here I will take a look at the lower and higer numbers 
I will start my left pointer at 0 and right pointer at left+1
then I will check while my right pinter is left than left pointer, 
if it is less then I will move my left pointer at my right pointer
now i will taverr my right pointer again and look if my 
profit = prices[right] - prices[left]
and I will also have a global maxProfit to maintain max profit
*/