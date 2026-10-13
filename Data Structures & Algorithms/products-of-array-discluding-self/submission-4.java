class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        //left product
        int leftProduct = 1;
        for(int i = 0; i<nums.length;i++){
            result[i] = leftProduct;
            leftProduct = leftProduct*nums[i];
        }
        //right product
        int rightProduct = 1;
        for(int j = nums.length-1; j>=0; j--){
            result[j]= result[j]*rightProduct;
            rightProduct = rightProduct*nums[j];
        }

        return result;
    }
}  
