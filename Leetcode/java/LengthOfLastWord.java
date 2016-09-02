public class LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        if (s.length() > 0) {
            boolean found = false;
            for (int i = 0; i < s.length() && !found; i++) {
                if (s.charAt(i) != ' ') {
                    found = true;
                }
            }
            if (found) {
                String[] wordList = s.split("\\s+");
                return wordList[wordList.length - 1].length();
            }
        }
        return 0;
    }
}
