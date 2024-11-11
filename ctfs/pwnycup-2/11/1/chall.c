#include <stdio.h>
#include <stdlib.h>

int main(char * argv);
int (*next)(char*) = &main;


int i=0;

char *spells[] = {
        "Expelliarmus",
        "Wingardium Leviosa",
        "Accio",
        "importantAdress",
        "Alohomora",
        "Expecto Patronum",
        "Avada Kedavra",
        "Crucio",
        "Stupefy",
        "Riddikulus",
        "Obliviate",
        "breakMainLoop",
        "/bin/sh",
        "Sectumsempra",
        "Reducto"
    };

int main(char * argv){ 
    printf("Hermione's book of spells \n");
    printf("> Spell number: %d\n",i+1);
    printf("> Spell name: %s\n",spells[i]);
    switch(i) {
        case 0:
            setbuf(stdout, NULL);
            printf("> Description: Disarms the opponent by removing their weapon.\n");
            break;
        case 1:
            printf("> Description: Causes objects to levitate.\n");
            break;
        case 2:
            printf("> Description: Summons objects towards the caster.\n");
            break;
        case 3:
            printf("> Description: No idea what is does , it only gives you this : %p and this : %p\n",puts,(void *)&next);
            break;
        case 4:
            printf("> Description: Unlocks doors or objects that are locked.\n");
            break;
        case 5:
            printf("> Description: Summons a protective Patronus against dark creatures.\n");
            break;
        case 6:
            printf("> Description: The Killing Curse, an unforgivable curse.\n");
            break;
        case 7:
            printf("> Description: Causes extreme pain to the target, another unforgivable curse.\n");
            break;
        case 8:
            printf("> Description: Stuns the target and renders them unconscious.\n");
            break;
        case 9:
            printf("> Description: Used to transform a boggart into something humorous.\n");
            break;
        case 10:
            printf("> Description: Erases the memory of the target.\n");
            break;
        case 11:
            printf("> Description: Let's you speak to He-Who-Must-Not-Be-Named so be wise !\n");
            fflush(stdout);
            char buf[256];
            fgets(buf, sizeof(buf), stdin); 
            printf(buf);
            break;
        case 12:
            printf("> Description: Opens a shell in proper conditions.\n");
            break;
        case 13:
            printf("> Description: Inflicts deep, slashing wounds on the target.\n");
            break;
        case 14:
            printf("> Description: Blasts solid objects to pieces.\n");
            break;
        default:
            break;
    }
    i++;
    if (i > 14) {
        printf("Bye , see you next time !\n");
        exit(0);
    }
    printf("\n[Press enter to move to next spell]");
    fflush(stdout);
    getchar();
    printf("\033[H\033[J");
    next(spells[i]);
}
