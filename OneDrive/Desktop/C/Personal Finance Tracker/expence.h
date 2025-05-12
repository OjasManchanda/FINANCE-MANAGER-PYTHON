#ifndef EXPENSE_H
#define EXPENSE_H

#define MAX_CATEGORY_LEN 50

// Structure to store an expense
typedef struct {
    float amount;
    char category[MAX_CATEGORY_LEN];
} Expense;

// Function declarations
void addExpense(char username[]);
void viewExpenses(char username[]);
void viewTotal(char username[]);

#endif
