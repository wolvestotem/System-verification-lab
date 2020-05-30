#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    /* Write your code here */

    /* Hints:
    *
    * 1. use argc and argv to access the command
    * line arguments of the program.
    *
    * 2. use getline and fputs functions to
    * read and respectively write a line to a file,
    * and strstr function to check if a string occurs
    * as a substring of other.
    */
    FILE *fr, *fw;

    char * line = NULL;
    size_t ll = 0;
    ssize_t read;

    fw = fopen("result.txt","w");

    if(!argv[1]){
        fclose(fw);
        return EXIT_SUCCESS;
    }

    fr = fopen("covid-confirmed-us-subset.txt","r");
    if(!fr){
        printf("ERROR: no such file");
        return EXIT_FAILURE;
    }

    char *key = argv[1];
    while ((read = getline(&line, &ll, fr)) != -1) {
        // printf("Retrieved line of length %zu:\n", read);
        // printf("%s", line);
        if(strstr(line,key)){
            fputs(line, fw);
        }
    }
    fclose(fr);
    fclose(fw);
    return EXIT_SUCCESS;
}
