public class RansomNote {
    public boolean canConstruct(String ransomNote, String magazine) {
        ArrayList<Character> letterList = new ArrayList<Character>();
        for (int i = 0; i < magazine.length(); i++) {
            letterList.add(magazine.charAt(i));
        }
        for (int i = 0; i < ransomNote.length(); i++) {
            boolean found = false;
            char target = ransomNote.charAt(i);
            for (int j = 0; j < letterList.size(); j++) {
                if (letterList.get(j) == target) {
                    found = true;
                    letterList.remove(j);
                    j = letterList.size();
                }
            }
            if (found == false) {
                return false;
            }
        }
        return true;
    }
}
