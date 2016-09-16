public class IntegerReplacement {
    public int integerReplacement(int n) {
        int count = 0;
        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
                count++;
            } else {
                int inc = n + 1;
                int dec = n - 1;
                int tempCount = 1;
                while (inc % 2 == 0 && dec % 2 == 0) {
                    inc >>= 1;
                    dec >>= 1;
                    tempCount++;
                }
                inc = Math.abs(inc);
                if (dec == 1) {
                    n = dec;
                } else if (inc == 1 || inc % 2 == 0) {
                    n = inc;
                } else {
                    n = dec;
                }
                count += tempCount;
            }
        }
        return count;
    }
}
