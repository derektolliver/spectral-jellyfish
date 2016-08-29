public class PowerOfFour {
    public boolean isPowerOfFour(int num) {
        double val = Math.log(num) / Math.log(4);
        if (Math.floor(val) == val && num != 0) {
            return true;
        } else {
            return false;
        }
    }
}
