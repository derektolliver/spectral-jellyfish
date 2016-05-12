public class MajorityElement {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> numFreq = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            if (numFreq.get(nums[i]) == null) {
                numFreq.put(nums[i], 1);
            } else {
                numFreq.put(nums[i], numFreq.get(nums[i]) + 1);
            }
        }

        int majEle = 0;
        int max = 0;
        for (Integer i : numFreq.keySet()) {
            if (numFreq.get(i) > max) {
                max = numFreq.get(i);
                majEle = i;
            }
        }

        return majEle;
    }
}
