public class FirstUniqueChar {
    public int firstUniqChar(String s) {
        int[] alpha = new int[26];
        for (int i = 0; i < s.length(); i++) {
            alpha[s.charAt(i) - 97]++;
        }
        for (int i = 0; i < s.length(); i++) {
            if (alpha[s.charAt(i) - 97] == 1) {
                return i;
            }
        }
        return -1;
    }
}
