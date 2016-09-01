public class ContainsNearbyDuplicate {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        if (nums.length > 0) {
            int old = nums[0];
            HashSet<Integer> kSet = new HashSet<Integer>();
            for (int i = 0; i < nums.length; i++) {
                if (kSet.contains(nums[i])) {
                    return true;
                }
                if (kSet.size() == k) {
                    kSet.remove(old);
                    old = nums[i - kSet.size()];
                }
                if (kSet.size() < k) {
                    kSet.add(nums[i]);
                }
            }
        }
        return false;
    }
}
