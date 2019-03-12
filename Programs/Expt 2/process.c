#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(){
    pid_t pid;
    int x = 1;
    pid = fork();
    if(pid < 0){ 
        printf("ERROR \n");
        exit(-1);
    }
    else if(pid == 0){
        printf("Child : \n PID is %d\nvalue of x is %d\n",getpid(),--x);
        exit(0);
    }else{
        //wait(NULL); 
        printf("Child over : \n");
        printf("Parent  : \nPID is %d\nvalue of x is %d\n",getpid(),++x);
    }

    return 0;
}