#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h> 

int main(int ac, char* av[])
{
    pid_t   pid, child_pid;

    while (1)
    {
        if (fork() == 0)
        {   
            /* child */
            printf("child process 'spid=%d\n",getpid());
            system("scrapy crawl newsSpider");
            break;
        } else {
            /* parent */
            child_pid = wait(NULL);
            printf("wait process 's pid=%d\n",child_pid); 
        }
    }
    return 0;
}

