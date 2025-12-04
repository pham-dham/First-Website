/* Menu Driven Activity
Programmer: Eryka Dib E. Garcia
BSIT 1A
Description: Assign grades to students at the end of the year. */
#include <stdio.h>

// Function to calculate and print the student's grade
void calculate_grade() {
    int student_number; // Variable to store the student's number
    float tutorial_mark;
    float test_mark;
    float exam_mark;
    float average;
    float final_mark;
    char grade;

    printf("\n--- Grade Calculation ---\n");
    printf("Enter student number: ");
    if (scanf("%d", &student_number) != 1) return; // Basic input check

    printf("Enter tutorial mark (0-100): ");
    if (scanf("%f", &tutorial_mark) != 1) return;

    printf("Enter test mark (0-100): ");
    if (scanf("%f", &test_mark) != 1) return;

    // Calculate the average of tutorial and test marks
    average = (tutorial_mark + test_mark) / 2.0; // Use 2.0 for float division

    // Early fail condition
    if (average < 40.0) {
        printf("\nRESULT: Student %d's average (%.2f) is below 40.\n", student_number, average);
        printf("RESULT: Student %d receives an **F** grade.\n", student_number);
        return;
    }

    printf("Enter examination mark (0-100): ");
    if (scanf("%f", &exam_mark) != 1) return;

    // Calculate the final mark based on weights
    // Weights: Tutorial (25%), Test (25%), Exam (50%)
    final_mark = (tutorial_mark * 0.25) + (test_mark * 0.25) +
                 (exam_mark * 0.50);

    // Assign a grade based on the final mark
    if (final_mark >= 80) {
        grade = 'A';
    } else if (final_mark >= 70) {
        grade = 'B';
    } else if (final_mark >= 60) {
        grade = 'C';
    } else if (final_mark >= 50) {
        grade = 'D';
    } else {
        grade = 'E'; // E for passing condition below 50 but above 40 average
    }

    // Print the final mark and grade
    printf("\n--- Final Results ---\n");
    printf("Student %d final mark is: **%.2f**\n", student_number,
           final_mark);
    printf("Student %d grade is: **%c**\n", student_number, grade);
    printf("---------------------\n");
}

int main() {
    int choice; // Variable to store user's menu choice

    // Use a do-while loop to display the menu until the user chooses to exit
    do {
        printf("\n======================\n");
        printf("       MENU\n");
        printf("======================\n");
        printf("1. Grade Student\n");
        printf("2. Exit Program\n");
        printf("Enter your choice: ");

        // Read choice and clear the input buffer afterward
        if (scanf("%d", &choice) != 1) {
            // Clear input buffer on failure to prevent infinite loop
            while(getchar() != '\n');
            choice = 0; // Set to invalid choice
        }

        // Use a switch statement to handle different menu choices
        switch (choice) {
            case 1:
                calculate_grade(); // Call the calculate_grade function
                break;
            case 2:
                printf("\nExiting program. Goodbye!\n");
                break;
            default:
                printf("\nInvalid choice. Please try again.\n");
        }
    } while (choice != 2); // Continue the loop until the user enters 2

    return 0; // Indicate that the program executed successfully
}