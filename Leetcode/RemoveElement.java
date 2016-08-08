public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        for (int i = 0; i < nums.length - count; i++) {
            if (nums[i] == val) {
                for (int j = i; j < nums.length - 1 - count; j++) {
                    nums[j] = nums[j + 1];
                }
                count++;
                i--;
            }
        }
        return nums.length - count;
    }
}
