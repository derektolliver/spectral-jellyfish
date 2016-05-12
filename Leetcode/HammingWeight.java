public class HammingWeight {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        String bits = Integer.toBinaryString(n);
        int numOnes = 0;
        for (int i = 0; i < bits.length(); i++) {
            if (bits.charAt(i) == '1') {
                numOnes++;
            }
        }
        return numOnes;
    }
}
