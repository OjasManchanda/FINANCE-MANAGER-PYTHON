#include <stdio.h>
#include <stdlib.h>
#include "user.h"
#include "expense.h"

int main() {
    User user;

    printf("Enter your name: ");
    scanf(" %[^\n]", user.name);  // allows spaces in name

    printf("Enter your email: ");
    scanf(" %s", user.email);

    if (userExists(user.name, user.email)) {
        printf("User already exists. Welcome back!\n");
    } else {
        generateUsername(user.email, user.username);
        printf("Registration successful!\nYour username is: %s\n", user.username);

        // Save new user to file
        FILE *fp = fopen("users.txt", "a");
        if (fp == NULL) {
            printf("Error opening file for writing.\n");
            return 1;
        }
        fprintf(fp, "%s %s %s\n", user.name, user.email, user.username);
        fclose(fp);
    }

    int choice;
do {
    printf("\n==== MENU ====\n");
    printf("1. Add Expense\n");
    printf("2. View All Expenses\n");
    printf("3. View Total Expense\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            addExpense(user.username);
            break;
        case 2:
            viewExpenses(user.username);
            break;
        case 3:
            viewTotal(user.username);
            break;
        case 4:
            printf("Exiting...\n");
            break;
        default:
            printf("Invalid choice!\n");
    }
} while (choice != 4);

    return 0;
}
