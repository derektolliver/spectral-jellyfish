public class PowerOfThree {
    public boolean isPowerOfThree(int n) {
        return n > 0 && (int) Math.pow(3, (int) (Math.log(Integer.MAX_VALUE) / Math.log(3.0))) % n == 0;
    }
}
