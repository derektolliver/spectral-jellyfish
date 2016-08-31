public class CountAndSay {
    public String countAndSay(int n) {
        String numString = "1";
        for (int i = 0; i < n - 1; i++) {
            StringBuffer result = new StringBuffer();
            char val = numString.charAt(0);
            int count = 1;
            for (int j = 1; j < numString.length(); j++) {
                if (val == numString.charAt(j)) {
                    count++;
                } else {
                    result.append(count);
                    result.append(val);
                    val = numString.charAt(j);
                    count = 1;
                }
            }
            result.append(count);
            result.append(val);
            numString = result.toString();
        }
        return numString;
    }
}
