#ifndef USER_H
#define USER_H

#define MAX_USERS 100
#define MAX_LEN 100

// User structure
typedef struct {
    char name[MAX_LEN];
    char email[MAX_LEN];
    char username[MAX_LEN];
} User;

// Function prototypes (declared, not defined)
void generateUsername(char email[], char username[]);
int userExists(char name[], char email[]);

#endif
