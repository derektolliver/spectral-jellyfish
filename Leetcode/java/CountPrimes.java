public class CountPrimes {
    public static int countPrimes(int n) {
        if (n == 0 || n == 1 || n == 2) {
            return 0;
        }
        int count = 0;
        boolean[] primeList = new boolean[n - 2];
        isPrime(fillArray(n), primeList);
        for (int i = 0; i < primeList.length; i++) {
            if (!primeList[i]) {
                System.out.println(i + 2);
                count++;
            }
        }
        return count;
    }

    private static ArrayList<Integer> fillArray(int n) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        result.add(2);
        for (int i = 3; i * i <= n; i++) {
            boolean composite = false;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    composite = true;
                }
            }
            if (!composite) {
                result.add(i);
            }
        }
        return result;
    }

    private static void isPrime(ArrayList<Integer> numCheck, boolean[] primeList) {
        for (int i = 0; i < primeList.length; i++) {
            int num = i + 2;
            for (int j = 0; j < numCheck.size() && primeList[i] == false && num != numCheck.get(j); j++) {
                if (num % numCheck.get(j) == 0) {
                    primeList[i] = true;
                }
            }
        }
    }
}
