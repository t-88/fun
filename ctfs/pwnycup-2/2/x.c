#include <stdlib.h>
#include <stdio.h>
#include <time.h>

__uint32_t FUN_00101209(void)
{
  time_t t;
  
  t = time((time_t *)0x0);
  return ((__uint32_t)(__uint8_t)((__uint64_t)t >> 0x30) | (__uint32_t)((__uint64_t)t >> 0x10)) << 0x10 &
         (__uint32_t)((__uint64_t)t >> 0x20) | 0xde;
}


void main () {

    // int a[] = {217,144,87,239,191,189,239,191,189,6,239,191,189,239,191,189,5,104,84,107,239,191,189,7,239,191,189,239,191,189,30,239,191,189,239,191,189,199,191,239,191,189,239,191,189,60,102,239,191,189,25,239,191,189,44,205,144,81,80,119,100,239,191,189,239,191,189,83,239,191,189,46,38,26,239,191,189,239,191,189,55,118,239,191,189,22};
    int a[] = {217,144,87,195,242,6,220,194,5,104,84,120};

    for(int j = 0; j < 1;j++) {
    int fa = 222;
    for(int i = 0; i < 12; i++) {
        srand(fa);
        char k = a[i];
        int rr = rand();
        k =  (char)rr ^ k ;
        fa = (__uint8_t)a[i];
        printf("%c",k);
    }
    printf("\n");
    }


    

    // printf()
    // printf("%d\n",FUN_00101209());
}