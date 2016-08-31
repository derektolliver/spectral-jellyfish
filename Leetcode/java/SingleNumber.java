public class SingleNumber {
    public int singleNumber(int[] nums) {
        ArrayList<Integer> numList = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (!numList.remove((Object) nums[i])) {
                numList.add(nums[i]);
            } else {
                numList.remove((Object) nums[i]);
            }
        }
        return numList.get(0);
    }
}
