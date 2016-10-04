import java.util.*;

public class LetterGen {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Welcome to the Lob Letter Generator! Please enter the following information to send your letter.");
        System.out.print("From Name: ");
        String name = scan.next();
        System.out.println();
        System.out.print("From Address Line 1: ");
        String address1 = scan.next();
        System.out.println();
        System.out.print("From Address Line 2: ");
        String address2 = scan.next();
        System.out.println();
        System.out.print("From City: ");
        String city = scan.next();
        System.out.println();
        System.out.print("From State ");
        String state = scan.next();
        System.out.println();
        System.out.print("From Zip Code: ");
        String zip = scan.next();
        System.out.println();
        System.out.print("Message: ");
        String message = scan.next();


    }

    public static HashMap<String, String> gatherInfo() {
        
    }

}
