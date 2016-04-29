public class ReverseVowels {
    public String reverseVowels(String s) {
        ArrayList<Character> toReverse = new ArrayList<Character>();
        char[] vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'};
        StringBuilder reversed = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < vowels.length; j++) {
                if (s.charAt(i) == vowels[j]) {
                    toReverse.add(s.charAt(i));
                    break;
                }
            }
        }

        int numMatches = toReverse.size() - 1;

        for (int i = 0; i < s.length(); i++) {
            boolean match = false;
            for (int j = 0; j < vowels.length; j++) {
                if (s.charAt(i) == vowels[j]) {
                    match = true;
                    break;
                }
            }
            if (match) {
                reversed.append(toReverse.get(numMatches));
                numMatches --;
            } else {
                reversed.append(s.charAt(i));
            }
        }

        return reversed.toString();
    }
}
