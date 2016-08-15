public class RemoveDuplicates {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        } else {
            ArrayList<Integer> nonDups = new ArrayList<Integer>();
            int temp = nums[0];
            nonDups.add(temp);
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] != temp) {
                    temp = nums[i];
                    nonDups.add(temp);
                }
            }
            for (int i = 0; i < nonDups.size(); i++) {
                nums[i] = nonDups.get(i);
            }
            return nonDups.size();
        }
    }
}
