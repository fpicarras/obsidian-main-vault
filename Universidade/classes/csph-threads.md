***
> Threads are software units of process that run instruction streams, in parallel. They are managed by the operating system

For example, an array that has N elements, instead of being processed in Serial, can be split for T threads and have an ideal speed-up of T.
Another useful example of threads are in user interfaces or network servers, threads can improve responsiveness by allowing background tasks to run without blocking the main thread.

# Concurrency

A big problem with threads is the access to shared resources, meaning: consider two threads that increment the same global variable, this threads will load the variable  

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

Threads are created using **pthread_create()**, which sets a variable of type **pthread_t**  to the reference of created thread. **pthread_create()** receives a thread function that will be executed in the spawned thread.
## Joining
- **pthread_join(pthread_t \*ptr, NULL)**

Will stop the program execution and wait for the thread to be complete. If by chance the thread gets stuck, **pthread_join** will not advance and the program will be stuck.
This command is useful because if the main ends before the threads the program will exit the execution context and the threads will be killed, therefore it is important that the program waits for the completion of the threads.

## Semaphores

Consider the following thread function:
```C
int counter = 0; // Shared resource 
pthread_mutex_t mutex; // Mutex to protect the shared resource

void* increment_counter(void* arg) { 
	for (int i = 0; i < 100000; ++i) { 
		// Lock the mutex before accessing the shared variable
		thread_mutex_lock(&mutex); 
		++counter; // Critical section 
		pthread_mutex_unlock(&mutex); // Unlock the mutex after accessing 
	} 
	return NULL; 
}
```

