#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<unistd.h>

void *threadfunc(void *var)
{
    printf("Thread from function %d \n ",var);
    sleep(1);
    printf("Exiting from function %d \n",var);

}

int main()
{
    pthread_t id;
    printf("Thread Created \n \n");
    for(int i=0;i<3;i++)
    {
    pthread_create(&id,NULL,threadfunc,i);   
    } 
    pthread_join(id,NULL);
    printf("Joined Thread \n \n ");
    
    exit(0);

}