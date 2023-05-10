#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "options.h"


Option options[OPTIONS_COUNT] = {
    {"-f", "--file"},
};

FILE *file;

int main(int argc, char** argv) {

    parseOptions(argc, argv);
    
    file = fopen(getOption("-f"), "r");
    
    puts(file);

    printf("letter: %s, word: %s, value: %s\n", options[0].letter, options[0].word, options[0].value);
    printf("Option: %s\n", getOption("--file"));
    return 0;
}