public class FactorialTrailingZeroes {
    public int trailingZeroes(int n) {
        int deg = 5;
        int div = n / deg;
        int result = div;
        while (div > 1) {
            deg *= 5;
            div = n / deg;
            result += div;
        }
        return result;
    }
}
