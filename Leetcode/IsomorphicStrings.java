public class IsomorphicStrings {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> letterMap = new HashMap<Character, Character>();
        for (int i = 0; i < s.length(); i++) {
            char key = t.charAt(i);
            char val = s.charAt(i);
            if ((letterMap.containsKey(key) && letterMap.get(key) != val) || (letterMap.containsValue(val) && !letterMap.containsKey(key))) {
                return false;
            } else {
                letterMap.put(t.charAt(i), s.charAt(i));
            }
        }
        StringBuffer resultGen = new StringBuffer();
        for (int i = 0; i < t.length(); i++) {
            resultGen.append(letterMap.get(t.charAt(i)));
        }
        return s.equals(resultGen.toString());
    }
}
