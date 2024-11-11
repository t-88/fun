#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 64
#define FLAG_SIZE 64

int main(){

    FILE *f = fopen("./flag.txt", "r");
    if (f == NULL) {
        perror("Create flag.txt in your local directory");
        return 1;
    }

    char *flag = (char *)malloc(FLAG_SIZE * sizeof(char));
    if (fgets(flag, FLAG_SIZE, f) == NULL) {
        perror("Error reading flag");
        free(flag);
        fclose(f);
        return 1;
    }
    fclose(f);
    
    char buf[BUFFER_SIZE];
    puts("How can you leak data off the stack ?");
    fflush(stdout);
    fgets(buf, sizeof(buf), stdin); 
    printf("Let's see if that worked : ");
    printf(buf);     
    free(flag);  
    return 0;
}

