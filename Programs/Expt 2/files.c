#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int fd,size;
    fd = open("sample.txt",O_RDONLY);
    if(fd == -1){
        printf("ERROR .... Exiting\n");
        exit(-1);
    }
    char *c;
    c = (char *)calloc(50, sizeof(char));
    size = read(fd,c,25);
    c[size] = '\0';
    
    printf("%d bytes read :  %s\n",size,c);
    close(fd);
    fd = open("sample2.txt",O_WRONLY | O_CREAT);
    if(fd == -1){
        printf("ERROR!! \n");
        exit(-1);
    }
    size = write(fd, "New content\n", strlen("New Content \n")); 
    printf("%d bytes written to file\n",size);
    close(fd);
}