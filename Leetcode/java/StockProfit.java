public class StockProfit {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int min = prices[0];
        int maxProf = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < min) {
                min = prices[i];
            } else {
                int newProf = prices[i] - min;
                if (newProf > maxProf) {
                    maxProf = newProf;
                }
            }
        }
        return maxProf;
    }
}
