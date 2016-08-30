public class FindTheDifference {
    public char findTheDifference(String s, String t) {
        int[] alpha1 = new int[26];
        int[] alpha2 = new int[26];
        char result = '0';
        for (int i = 0; i < s.length(); i++) {
            char index = (char) (s.charAt(i) - 97);
            alpha1[index]++;
        }
        for (int i = 0; i < t.length(); i++) {
            char index = (char) (t.charAt(i) - 97);
            alpha2[index]++;
        }
        for (int i = 0; i < alpha1.length; i++) {
            if (alpha1[i] != alpha2[i]) {
                result = (char) (i + 97);
            }
        }
        return result;
    }
}
