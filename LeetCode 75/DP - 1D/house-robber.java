class Solution {
    public int rob(int[] nums) {
        ArrayList<Integer> cars = new ArrayList<Integer>();

        if(nums.length == 0){
            return 0;
        }
        else if(nums.length == 1){
            return nums[0];
        }

        cars.add(nums[0]);
        cars.add(nums[0] > nums[1] ? nums[0] : nums[1]);
        for(int i = 2; i < nums.length; i++){
            int val1 = nums[i] + cars.get(i-2);
            int val2 = cars.get(i-1);
            cars.add(i, val1 > val2 ? val1 : val2);
        }

        return Collections.max(cars);
    }
}