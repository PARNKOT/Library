#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <time.h>
#include <sys/time.h>
#include "options.h"


void mainLoop();
void compareStrings(char* s1, char* s2);
int compareWords(char *word1, char *word2);


Option options[OPTIONS_COUNT] = {
    {"-f", "--file"},
};

FILE *file;

void print_file(FILE *file) {
    char *line = NULL;
    size_t len = 0;
    
    while(getline(&line, &len, file) != -1) {
        printf("%s", line);
    }

    if (line) {
        free(line);
    }

}

int main(int argc, char** argv) {
    parseOptions(argc, argv);
    
    if (file = fopen(getOption("-f"), "r")) {
        mainLoop();
        fclose(file);
    } else {
        perror("Couldn't open file");
    }

    return 0;
}


void mainLoop() {
    char *file_line = NULL;
    char *user_line = NULL;

    struct timeval tv_start, tv_end;
    long seconds, micros;

    size_t previous_len = 0,
           current_len = 0;
    
    while(getline(&file_line, &current_len, file) != -1) {
        if (user_line && (current_len == previous_len)) {
            user_line = (char*)realloc(user_line, sizeof(char)*current_len);
        } else if (!user_line) {
            user_line = (char*)malloc(sizeof(char)*current_len);
        }
        previous_len = current_len;
        
        printf("==============================================\n");
        printf("-> %s", file_line);
        printf("Your turn:\n");

        gettimeofday(&tv_start, NULL);

        scanf("%[^\n]%*c", user_line);

        gettimeofday(&tv_end, NULL);
        diff = tv_end.tv_sec + 
        long seconds = (tv_end.tv_sec - tv_start.tv_sec);
        long micros = ((seconds * 1000000) + tv_end.tv_usec) - (tv_start.tv_usec);

        compareStrings(file_line, user_line);
        //printf("Time: %ld s %ld ms\n", seconds, micros);
        printf("Time: %ld ms\n", micros/1000);
        
        #ifdef DEBUG
        printf("-> %s\n", user_line);
        #endif
        
        printf("==============================================\n");
    }

    if (file_line) {
        free(file_line);
    }
}


#if __linux__ || __unix || __unux__

void compareStrings(char* base, char* s) {
    char *word1, *word2;
    char *last1, *last2;
    int matches = 0;
    int sum_length = 0;

    word1 = __strtok_r(base, " ,", &last1);
    word2 = __strtok_r(s, " ,", &last2);
    while( word1 != NULL && word2 != NULL ) {
        sum_length += strlen(word1);
        matches += compareWords(word1, word2);

        word1 = __strtok_r(NULL, " ", &last1);
        word2 = __strtok_r(NULL, " ", &last2);
    }

    while(word1 != NULL) {
        sum_length += strlen(word1) - 1;
        word1 = __strtok_r(NULL, " ", &last1);
    }

    printf("Percent: %i %% \n", matches*100/(sum_length-1));
}

#elif _WIN32 || _WIN64
// char* strtok_s(char* s, char *delim, char** last) {
//     if (s) {
//         int count = 0;

//         while(*s != *delim) {
//             count ++;
//         }

//         return
//     }
    
//     if (*s == '\0') {
//         return NULL;
//     }
// }

// int strtok_my(char **s, char delim) {
//     while(**s != delim) {
//         if (**s == '\0') {
//             return 0;
//         }

//         ++(*s);
//     }

//     return 1;
// }

void compareStrings(char* base, char* s) {
    char *word1, *word2;
    char *last1, *last2;
    int matches = 0;
    int sum_length = 0;
    
    word1 = __strtok_r(base, " ,", &last1);
    word2 = __strtok_r(s, " ,", &last2);
    while( word1 != NULL && word2 != NULL ) {
        sum_length += strlen(word1);
        matches += compareWords(word1, word2);

        word1 = __strtok_r(NULL, " ", &last1);
        word2 = __strtok_r(NULL, " ", &last2);
    }

    while(word1 != NULL) {
        sum_length += strlen(word1) - 1;
        word1 = __strtok_r(NULL, " ", &last1);
    }

    printf("Percent: %i %% \n", matches*100/(sum_length-1));
}

#endif



int compareWords(char *word1, char *word2) {
    int count_matches = 0;
    
    while(*word1 != '\0' && *word2 != '\0') {
        *word1 == *word2 ? ++count_matches : 0;
        ++word1;
        ++word2;
    }

    return count_matches;
}
