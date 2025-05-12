#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "user.h"

// Function to generate username from email
void generateUsername(char email[], char username[]) {
    int i = 0;
    while (email[i] != '@' && email[i] != '\0') {
        username[i] = email[i];
        i++;
    }
    username[i] = '\0';
}

// Function to check if user exists in file
int userExists(char name[], char email[]) {
    FILE *fp = fopen("users.txt", "r");
    if (!fp) return 0; // File doesn’t exist yet

    char file_name[MAX_LEN], file_email[MAX_LEN], file_username[MAX_LEN];
    while (fscanf(fp, "%s %s %s", file_name, file_email, file_username) != EOF) {
        if (strcmp(name, file_name) == 0 && strcmp(email, file_email) == 0) {
            fclose(fp);
            return 1; // User found
        }
    }
    fclose(fp);
    return 0; // Not found
}

// Main program
int main() {
    User user;

    printf("Enter your name: ");
    scanf(" %[^\n]", user.name);  // Read full name with spaces

    printf("Enter your email: ");
    scanf(" %s", user.email);

    if (userExists(user.name, user.email)) {
        printf("User already exists. Welcome back!\n");
    } else {
        generateUsername(user.email, user.username);
        printf("Registration successful!\nYour username is: %s\n", user.username);

        // Save to file
        FILE *fp = fopen("users.txt", "a");
        if (fp == NULL) {
            printf("Error opening file.\n");
            return 1;
        }
        fprintf(fp, "%s %s %s\n", user.name, user.email, user.username);
        fclose(fp);
    }

    return 0;
}
