public class NumArray {

    private int[] numMap;

    public NumArray (int[] nums) {
        numMap = new int[nums.length];
        int currSum = 0;
        for (int i = 0; i < nums.length; i++) {
            currSum += nums[i];
            numMap[i] = currSum;
        }
    }

    public int sumRange(int i, int j) {
        if (i == 0) {
            return numMap[j];
        }
        return numMap[j] - numMap[i - 1];
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
