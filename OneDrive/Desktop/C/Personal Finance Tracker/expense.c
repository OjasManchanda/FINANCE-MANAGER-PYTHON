#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "expense.h"

void addExpense(char username[]) {
    Expense exp;
    printf("Enter expense amount: ");
    scanf("%f", &exp.amount);
    printf("Enter expense category: ");
    scanf(" %[^\n]", exp.category);

    FILE *fp = fopen("expenses.txt", "a");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    fprintf(fp, "%s %.2f %s\n", username, exp.amount, exp.category);
    fclose(fp);
    printf("Expense added successfully!\n");
}

void viewExpenses(char username[]) {
    FILE *fp = fopen("expenses.txt", "r");
    if (fp == NULL) {
        printf("No expenses found.\n");
        return;
    }

    char file_username[100];
    Expense exp;
    int found = 0;

    printf("\nYour Transactions:\n");
    printf("---------------------\n");
    while (fscanf(fp, "%s %f %[^\n]", file_username, &exp.amount, exp.category) != EOF) {
        if (strcmp(username, file_username) == 0) {
            printf("Amount: ₹%.2f | Category: %s\n", exp.amount, exp.category);
            found = 1;
        }
    }

    if (!found) {
        printf("No transactions yet.\n");
    }

    fclose(fp);
}

void viewTotal(char username[]) {
    FILE *fp = fopen("expenses.txt", "r");
    if (fp == NULL) {
        printf("No expenses found.\n");
        return;
    }

    char file_username[100];
    Expense exp;
    float total = 0;

    while (fscanf(fp, "%s %f %[^\n]", file_username, &exp.amount, exp.category) != EOF) {
        if (strcmp(username, file_username) == 0) {
            total += exp.amount;
        }
    }

    printf("Total expenses: ₹%.2f\n", total);
    fclose(fp);
}
