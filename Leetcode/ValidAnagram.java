public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if (s.length() == t.length()) {
            char[] sLetters = s.toCharArray();
            char[] tLetters = t.toCharArray();
            Arrays.sort(sLetters);
            Arrays.sort(tLetters);

            for (int i = 0; i < sLetters.length; i++) {
                if (sLetters[i] != tLetters[i]) {
                    return false;
                }
            }

            return true;
        } else {
            return false;
        }
    }
}
