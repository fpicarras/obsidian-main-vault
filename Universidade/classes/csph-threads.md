***
> Threads are software units of process that run instruction streams, in parallel. They are managed by the operating system

For example, an array that has N elements, instead of being processed in Serial, can be split for T threads and have an ideal speed-up of T.
Another useful example of threads are in user interfaces or network servers, threads can improve responsiveness by allowing background tasks to run without blocking the main thread.

# pthreads

>Or POSIX threads, are the standard milti-threading in C.
```C
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* print_message(void* message) {
    printf("%s\n", (char*)message);
    return NULL;
}

int main() {
    pthread_t thread1, thread2;

    // Create two threads
    pthread_create(&thread1, NULL, print_message, "Hello from Thread 1");
    pthread_create(&thread2, NULL, print_message, "Hello from Thread 2");

    // Wait for both threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}
```

## Creation
- **pthread_create(pthread_t \*ptr, NULL,0 thread_function, void \*args)**

Threads are created using **pthread_create()**, which sets a variable of type **pthread_t**  to the reference of created thread. **pthread_create()** recieves a thread function that wi