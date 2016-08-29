import java.util.Scanner;

public class WordPattern {
    public boolean wordPattern(String pattern, String str) {
        HashMap<Character, String> patternMap = new HashMap<Character, String>();
        ArrayList<String> wordList = new ArrayList<String>();
        Scanner strScan = new Scanner(str);
        while (strScan.hasNext()) {
            wordList.add(strScan.next());
        }
        if (pattern.length() != wordList.size()) {
            return false;
        }
        for (int i = 0; i < pattern.length(); i++) {
            char key = pattern.charAt(i);
            boolean complete = false;
            String word = wordList.get(i);
            if (!patternMap.containsKey(key) && !patternMap.containsValue(word)) {
                patternMap.put(key, word);
            } else if (!(patternMap.containsKey(key) && patternMap.get(key).equals(word))) {
                return false;
            }
        }
        return true;
    }
}
