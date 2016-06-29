public class HappyNum {
    public boolean isHappy(int n) {
        HashSet<Integer> possRepeats = new HashSet<Integer>();
        while (n != 1) {
            if (possRepeats.contains(n)) {
                return false;
            }
            possRepeats.add(n);
            int newNum = 0;
            while (n != 0) {
                newNum += Math.pow(n % 10, 2);
                n /= 10;
            }
            n = newNum;
        }
        return true;
    }
}
