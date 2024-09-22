***
> Threads are software units of process that run instruction streams, in parallel. They are managed by the operating system

For example, an array that has N elements, instead of being processed in Serial, can be split for T threads and have an ideal speed-up of T.
Another useful example of threads are in user interfaces or network servers, threads can improve responsiveness by allowing background tasks to run without blocking the main thread.

# Concurrency

A big problem with threads is the access to shared resources, meaning: consider two threads that increment the same global variable, this threads will load the variable (which at the time has value *X*) and increment it, now both have value *X+1* then they store it.
Notice the problem: it was supposed to have value *X+2* but because the threads operated in the same variable at the same time there was a data corruption.
This is called a **critical section**, it is where multiple threads modify a shared resource. In order to prevent it's corruption we have to use **Semaphores** to coordinate the access to the variable.

## False Sharing

Consider that the threads write in different position of the array. What happens now is that when a thread writes to that variable, the cache line (which contains the array) will be dirty, hence, all the other threads need to update it's cache.
Although methods like this are each ways to modify global variables without corruption (because they are not writing in the same position), they make the program slower because of the consecutive memory updates needed to be done.
***
# C pthreads

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

We are using a **mutex** to lock a critical region: when a thread attempts to enter the critical region, it has to lock the mutex, do the code and then unlock it. If by chance there is a thread already in the critical region, thread that wanted to lock it will have to wait in a queue for it's turn. Much like we wait in line for a public bathroom.
***
# C++11 Threads

This function exactly the same way as **pthreads** but it is easier to understand.

```Cpp
#include <iostream>
#include <thread>
#include <mutex>

int counter = 0;  // Shared resource
std::mutex mtx;   // Mutex to protect the shared resource

void increment_counter() {
    for (int i = 0; i < 100000; ++i) {
        std::lock_guard<std::mutex> lock(mtx);  // Automatically locks and unlocks
        ++counter;  // Critical section
    }
}

int main() {
    // Create two threads
    std::thread thread1(increment_counter);
    std::thread thread2(increment_counter);

    // Wait for both threads to finish
    thread1.join();
    thread2.join();

    // Print the final value of the counter
    std::cout << "Final counter value: " << counter << std::endl;

    return 0;
}
```

The syntax is different, but the concept is the same.

## std::thread
Is the variable type, that store a reference to a spawned thread.

## std::thread(thread_function, args)
Returns a thread reference and executes *thread_function* with has many arguments has we want.

## .join()
Is a method (from the *std::thread* object) that waits for the respective thread's completion.

## std::mutex
Are a bit more complicated, they lock an entire scope, when that variable goes out of scope, the mutex is unlocked.