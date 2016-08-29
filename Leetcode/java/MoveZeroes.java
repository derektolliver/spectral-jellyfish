public class MoveZeroes {
    public void moveZeroes(int[] nums) {
        int numZeroes = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0 && numZeroes > 0) {
                nums[i - numZeroes] = nums[i];
                nums[i] = 0;
            } else if (nums[i] == 0) {
                numZeroes++;
            }
        }
    }
}
