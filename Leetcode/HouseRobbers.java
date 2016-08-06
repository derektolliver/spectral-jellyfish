public class HouseRobbers {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        } else if (nums.length == 1) {
            return nums[0];
        } else {
            int[] results = new int[nums.length];
            int max;
            results[0] = nums[0];
            if (nums[0] > nums[1]) {
                max = nums[0];
            } else {
                max = nums[1];
            }
            results[1] = max;
            for (int i = 2; i < nums.length; i++) {
                int temp = 0;
                int prev = results[i - 1];
                if (nums[i] + results[i - 2] > prev) {
                    temp = nums[i] + results[i - 2];
                } else {
                    temp = prev;
                }
                results[i] = temp;
            }
            return results[nums.length - 1];
        }
    }
}
