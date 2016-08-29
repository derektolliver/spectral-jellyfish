public class BullsAndCows {
    public String getHint(String secret, String guess) {
        int bulls = 0;
        int cows = 0;
        ArrayList<Character> secretList = new ArrayList<Character>();
        ArrayList<Character> guessList = new ArrayList<Character>();
        for (int i = 0; i < secret.length(); i++) {
            if (secret.charAt(i) == guess.charAt(i)) {
                bulls++;
            } else {
                secretList.add(secret.charAt(i));
                guessList.add(guess.charAt(i));
            }
        }
        for (int i = 0; i < secretList.size(); i++) {
            boolean found = false;
            for (int j = 0; j < guessList.size(); j++) {
                if (secretList.get(i) == guessList.get(j)) {
                    cows++;
                    guessList.remove(j);
                    j = guessList.size();
                }
            }
            if (found) {
                secretList.remove(i);
            }
        }
        StringBuilder resultGen = new StringBuilder();
        resultGen.append(bulls);
        resultGen.append("A");
        resultGen.append(cows);
        resultGen.append("B");
        return resultGen.toString();
    }
}
