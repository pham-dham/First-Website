package formletterwriter;

import java.util.Scanner;

/**
 * Activity 3: Form Letter Writer
 * Programmer: Erryka Dib E. Garcia
 * Description: Demonstrates method overloading with two displaySalutation methods.
 */
public class FormLetterWriter {

    // display salutation with only last name (formal, Mr./Ms.)
    public void displaySalutation(String lastName) {
        System.out.println("Dear Mr. or Ms. " + lastName);
        System.out.println("Thank you for your recent order.");
    }

    // display salutation with first and last name (personal)
    public void displaySalutation(String firstName, String lastName) {
        System.out.println("Dear " + firstName + " " + lastName);
        System.out.println("Thank you for your recent order.");
    }

    public static void main(String[] args) {
        // Initialize Scanner for user input
        Scanner scanner = new Scanner(System.in);
        // Create an instance of the class to call the methods
        FormLetterWriter writer = new FormLetterWriter();

        // --- Test Case 1: Formal Salutation (Last Name Only) ---
        System.out.println("--- Formal Salutation ---");
        System.out.print("Enter the last name: ");
        String lastName1 = scanner.nextLine();
        
        // Calls the displaySalutation(String lastName) overload
        writer.displaySalutation(lastName1);

        System.out.println("\n----------------------------------\n");
        
        // --- Test Case 2: Personal Salutation (First and Last Name) ---
        System.out.println("--- Personal Salutation ---");
        System.out.print("Enter the first name: ");
        String firstName2 = scanner.nextLine();
        System.out.print("Enter the last name: ");
        String lastName2 = scanner.nextLine(); 
        
        // Calls the displaySalutation(String firstName, String lastName) overload
        writer.displaySalutation(firstName2, lastName2);

        // Close the scanner
        scanner.close();
    }
}